[Home](/) > [Engineering](/engineering/) > [Infrastructure](/engineering/infrastructure/) > bare-for-pear

# bare-for-pear

Modules built for the Bare runtime — a mix of community forks (Node.js assumptions stripped, Bare's minimal API surface honoured) and infrastructure modules (original pieces for the bare-for-pear ecosystem). SPLectrum uses these as constitutive dependencies, vendored into the runtime repo.

## Modules

- [avsc](avsc/) — Avro type system, serialization, schema evolution.
- [avsc-rpc](avsc-rpc/) — Avro RPC protocol, service definition, transports.
- [git](git/) — git operations, subtree management, two-reality model.
- [rpc-server](rpc-server/) — server lifecycle, PID management, file-based command IPC.
