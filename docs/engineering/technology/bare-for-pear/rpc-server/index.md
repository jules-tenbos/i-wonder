[Home](/) > [Engineering](/engineering/) > [Technology](/engineering/technology/) > [bare-for-pear](/engineering/technology/bare-for-pear/) > RPC Server

# RPC Server — Lifecycle Module

Server lifecycle management for the Bare runtime. TCP listener management, PID tracking, file-based command IPC, and request logging. One of the constitutive bare-for-pear modules.

Source: [bare-for-pear/rpc-server](https://github.com/bare-for-pear/rpc-server)

---

## Why a Server Module

The server started as a 57-line file that mixed TCP setup, RPC wiring, logging, and dispatch. No way to stop it cleanly. No way to tell if it was running. No way to restart without killing the process. Every session began with `pkill bare` and ended with the same.

The extraction follows the same pattern as the git module: infrastructure in lib/, thin protocol layer in spl/. After extraction, the protocol layer is ~20 lines that wire the avsc-rpc service to the infrastructure. The server module knows nothing about AVRO, RPC protocols, or dispatch.

The boundary is `onConnection(socket)`. The module manages TCP. The caller creates whatever protocol channels it needs on the socket. This separation means the module is useful for any TCP server on Bare, not just the spl RPC server.

---

## File-Based Command IPC

The standard ways to talk to a running server — signals, IPC sockets, HTTP endpoints — all require either platform-specific APIs or additional dependencies. Bare has limited signal support. Unix domain sockets need bare-pipe configuration. An HTTP endpoint is a whole additional server.

Files are simpler. The server watches `_server/cmd/` for file creation. Drop a file named `shutdown`, the server shuts down. Drop `restart`, it restarts. The file is consumed (deleted) after processing.

This is debuggable in a way that signals never are. `ls _server/cmd/` shows pending commands. `touch _server/cmd/shutdown` works from any shell, any script, any process. The mechanism is visible, stateless, and self-documenting.

The watcher scans for existing files on startup. If a command was written before the watcher started, it still gets processed. No race condition between writing and watching.

---

## PID as Process Identity

The server writes `Bare.pid` to `_server/pid` on start, removes it on clean shutdown. This gives any other process — the test runner, a monitoring script, the CLI — a way to know if the server is alive without making a TCP connection.

`pid.alive()` reads the PID file and tests the process with `os.kill(pid, 0)` — signal 0 doesn't kill, just checks existence. If the process is gone (crashed without cleanup), the PID file is stale. The next `start()` detects this, cleans the stale file, and proceeds.

The PID check is instant. The TCP fallback (connect and disconnect) takes network round-trip time and can hang on half-open connections. For the test runner, which checks server availability before every run, the difference matters.

---

## Design Decisions

**Singleton per process.** One server instance, module-level state. There's no use case for multiple TCP servers in the same Bare process. The simplicity of `rpcServer.start()` / `rpcServer.stop()` follows from this.

**Protocol-agnostic.** The `onConnection` callback is the only protocol surface. The module creates and manages TCP connections. What runs on them is the caller's concern. Today it's avsc-rpc channels. Tomorrow it could be anything.

**Render parameter on logging.** The log function takes an optional render function that transforms the message before writing to disk. This keeps the display module (which knows about AVRO schemas and human-readable formatting) in the spl layer. The infrastructure module writes whatever JSON it's given.

**Graceful shutdown.** `tcpServer.close()` waits for active connections to drain before closing. If a request is in flight, it completes. The PID file is removed in the close callback, not before — the server is only declared stopped when it actually is.

