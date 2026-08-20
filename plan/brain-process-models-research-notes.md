# Brain process models — research notes (entry-depth round)

Research round completed 2026-08-20. Scope decision: entry depth only — enough for a meaningful cognition subject entry per model plus honest person pages; not a deep dive into any framework's internal disputes. Deliverables this round feeds: Friston person page, Baars person page (Dehaene named and external-linked, revisit if standing proves co-equal), three model entries on the cognition subject's sciences side, and internal links into the survey post.

---

## 1. Edelman — theory of neuronal group selection (TNGS / "Neural Darwinism")

**Core claim.** The brain is a somatic selective system, not an instructional one: pre-existing variant circuitry is differentially amplified by experience. Development generates a *primary repertoire* of variant neuronal groups; experience selects among them by synaptic strengthening/weakening, yielding a *secondary repertoire*; *reentry* — massively parallel recursive signalling between reciprocally mapped areas — correlates the selected maps into coherent function. First formulated Edelman & Mountcastle 1978 (*The Mindful Brain*); full statement *Neural Darwinism* (Basic Books, 1987) — the book title the field adopted as the theory's name.

**Mechanism, Edelman's terms.** (i) Developmental selection: epigenetic variation (cell division, migration, programmed death, axon/dendrite growth, CAMs/topobiology) produces degenerate, individually unique primary repertoires. (ii) Experiential selection in "somatic time": behaviour modifies synaptic populations; value systems (diffuse ascending neuromodulation) bias the selection. (iii) Reentrant signalling grounds perceptual categorisation without a homunculus; memory is "recategorisation," not a replicative store. Edelman insisted reentry ≠ feedback (feedback is serial and error-driven).

**Evidence — honest read.** Consistency-with-known-facts plus simulation, not direct tests. Consistent: developmental exuberance and pruning, individual variability of cortical maps, Merzenich-style map plasticity. Main empirical arm is his own group's Darwin series of brain-based devices (Darwin III sensorimotor automaton; Darwin IV real-world tracking robot, PNAS 1992; Darwin VII conditioning; Darwin X hippocampal spatial memory). These are existence proofs that selectionist architectures can produce adaptive categorisation — not tests discriminating TNGS from alternatives. No experiment has isolated "neuronal groups" as units of selection.

**Criticism.** Crick, "Neural Edelmanism," *Trends in Neurosciences* 12(7):240–248, 1989 (verified): the connectivity change in Edelman's own simulations is too great to count as selection of pre-existing groups — synapse selection at most, "group formation" the honest term; without a replicator the Darwin label is rhetorical. Underdetermination charge: experiential "selection" is implemented as synaptic weight change, so what empirically distinguishes selectionism from instructionist learning accounts? Fernando, Szathmáry & Husbands (*Front. Comput. Neurosci.* 2012): true Darwinian dynamics need replication of units, which TNGS lacks. (Purves constructivist-growth and Barlow group-concept criticisms circulate but exact citations unverified this round — confirm before use.)

**AI reception.** Lottery Ticket Hypothesis (Frankle & Carbin, ICLR 2019) has an obvious structural rhyme (dense random init ≈ primary repertoire; winning ticket ≈ selected subnetwork), and Edelman 1987 is cited in some LTH-adjacent papers — but the connection is peripheral/informal, not in Frankle & Carbin and not a mainstream thread. Neuroevolution/NAS echo selectionism generically, without lineage claims.

**Later trajectory (beyond scope).** Reentry became load-bearing for the consciousness work: Tononi & Edelman dynamic core (*Science* 1998; *A Universe of Consciousness* 2000); Tononi's IIT descends from this line.

**Status today.** Largely historical as a named theory; its uncontroversial parts (pruning, degeneracy, map plasticity, recurrent signalling, value-modulated plasticity) absorbed without the branding. Live niches: developmental motor assessment (Hadders-Algra NGST), neurorobotics lineage, dynamic-core→IIT descent.

**Person-page facts.** Nobel 1972 Physiology or Medicine, shared with Rodney Porter, for the *chemical structure of antibodies* — NOT for clonal selection itself (the selection-not-instruction insight is the intellectual bridge he walked, but the prize citation is structure). Books: Neural Darwinism 1987, Topobiology 1988, The Remembered Present 1989, Bright Air Brilliant Fire 1992, A Universe of Consciousness (w/ Tononi) 2000, Wider than the Sky 2004, Second Nature 2006. Founded The Neurosciences Institute.

---

## 2. Global Workspace Theory — Baars; Global Neuronal Workspace — Dehaene/Changeux

**Core claim.** Baars 1988 (*A Cognitive Theory of Consciousness*): many specialised unconscious processors run in parallel; they compete for access to a limited-capacity global workspace; the winner is broadcast brain-wide — globally available to attention, memory, report, motor systems — and that global availability is (functionally) what consciousness is. Inspired by AI blackboard architectures.

**Mechanism.** Baars: theatre metaphor (1997). Dehaene–Changeux–Naccache Global Neuronal Workspace (canonical: Dehaene & Naccache 2001, *Cognition*): workspace = long-range excitatory neurons (layer II/III pyramidal), concentrated fronto-parietal. Signature: conscious access = late (~300ms), nonlinear, all-or-none "ignition"; scalp correlate P3b. Standard statement Dehaene & Changeux 2011 (*Neuron*).

**Evidence.** Masking: Dehaene et al. 2001 (*Nat. Neurosci.*) — masked words weak/local, visible words widespread parieto-frontal. Attentional blink: Sergent, Baillet & Dehaene 2005 — early ERP identical seen/blinked, P3b only on seen. Threshold masking: Del Cul et al. 2007 (*PLoS Biol*) — sigmoidal all-or-none ignition tracking visibility. General: unconscious processing preserved ~200ms local; conscious adds the late global wave.

**Criticism.** (a) Report confound: frontal activity/P3b may index reporting, not awareness (Tsuchiya, Wilke, Frässle & Lamme 2015, *TiCS*); no-report studies (Pitts 2014, Cohen 2020) find no P3b for seen-but-task-irrelevant stimuli — hitting the canonical signature. Counter (Block, Overgaard): task-irrelevant stimuli may also not be *accessed*. (b) Access vs phenomenal (Block 1995/2007): GWT at best a theory of access consciousness; experience may overflow access. Dehaene bites the bullet: reportable access is the tractable notion. (c) Cogitate adversarial collaboration (IIT vs GNWT; *Nature* 642:133–142, 2025, n=256): partial support for PFC content (present but less than predicted), clear failure of the predicted second ignition at stimulus offset. Consensus: challenged both theories, refuted neither. Beware press overclaiming.

**AI reception (verified).** Bengio "The Consciousness Prior" (arXiv 1709.08568) explicitly GWT-anchored; Goyal/Bengio shared-global-workspace transformers (ICLR 2022); VanRullen & Kanai "Deep learning and the Global Workspace Theory" (*TiNS* 2021); Butlin/Long 2023 consciousness-in-AI report uses GWT as an indicator-property theory. LeCun is *not* a GWT adopter — mentions in commentary only.

**Person-page facts — Baars.** b. 1946 Amsterdam, emigrated to California 1958; Dutch-American; PhD UCLA (psycholinguistics; early work on speech errors). Wright Institute (Berkeley; medium confidence — widely stated); later senior fellow in theoretical neurobiology, The Neurosciences Institute, San Diego — *with Edelman*, a nice on-site connection. Undisputed originator of GWT. Works: A Cognitive Theory of Consciousness 1988; In the Theater of Consciousness 1997; "The conscious access hypothesis" (*TiCS* 2002); On Consciousness 2019. Co-founded ASSC and *Consciousness and Cognition*.

**Person-page facts — Dehaene.** b. 1965, French; maths (ENS) → cognitive psychology (Mehler) → postdoc Changeux. Collège de France chair of Experimental Cognitive Psychology (2005–, created for him); director NeuroSpin; Brain Prize 2014. Books: The Number Sense 1997, Reading in the Brain 2009, Consciousness and the Brain 2014, How We Learn 2020, Seeing the Mind 2023. Contribution: the neural mechanism + experimental program. Field usage: GNW usually treated as GWT's neural implementation, though theory comparisons list GNWT separately (PFC-centric, all-or-none ignition) with Dehaene as lead proponent.

**Relationship.** Cordial, mutually citing, no priority dispute; Dehaene 2001 credits Baars explicitly. Divergence is emphasis: Baars cortex-wide/thalamocortical, Dehaene prefrontal-parietal.

---

## 3. Friston — free energy principle; predictive coding

**Core claim.** Self-organising systems that persist must act as if minimising variational free energy — an upper bound on surprise (negative log model evidence) of sensory states. Perception = updating generative-model beliefs; action = changing input to match predictions (active inference). Cortically: predictions descend, errors ascend. Milestones: Friston 2005 (*Phil Trans R Soc B*), Friston/Kilner/Harrison 2006 (*J Physiol Paris*), Friston 2010 (*Nat Rev Neurosci*).

**Principle vs process theory — the load-bearing distinction.** The PRINCIPLE is mathematical/normative, arguably true by construction, not empirically testable — Friston concedes it is "not falsifiable, like Hamilton's principle of least action"; principles are judged by usefulness. PROCESS THEORIES make testable predictions: predictive coding is the leading one, with its own pre-FEP lineage (Rao & Ballard 1999, *Nat. Neurosci.*, hierarchical predictive coding of visual cortex) later absorbed into FEP. Andrews ("The math is not the territory," *Biology & Philosophy* 2021): falsifiability demands on FEP rest on a category error.

**Evidence (for predictive coding, NOT the principle).** Repetition suppression — supported but interpretation contested (Tang et al., *eLife* 2018: prediction error and repetition suppression dissociable). Mismatch negativity — standard showcase (Garrido 2009 lineage; schizophrenia modelling). Laminar story (errors superficial/ascending, predictions deep/descending) — evidence MIXED: some recordings support, but e.g. rodent mPFC found no superficial/deep differences (*PLOS Biology* 2020). Fair statement: suggestive support, not settled (cf. Heilbron & Chait 2018 asking the question seriously).

**Criticism.** Unfalsifiability charge widely made (Colombo & Wright, *Synthese* 2021; Entropy 2021 "Good Science and Questionable Philosophy"). Markov blanket dispute: Bruineberg, Dołęga, Dewhurst & Baltieri, "The Emperor's New Markov Blankets," *BBS* 2022 — the literature conflates the modest statistical construct (Pearl blanket) with a metaphysically loaded organism/mind boundary (Friston blanket); the ontological conclusions don't follow from the math. Enactivist pushback: Di Paolo/Thompson reject the internalist/representationalist reading; some (Bruineberg, Kirchhoff, Ramstead) attempt enactive readings — compatibility contested. **Dopamine RPE — keep distinct:** Schultz, Dayan & Montague 1997 (*Science*): midbrain dopamine neurons signal reward prediction error matching TD learning — single-unit, quantitative, replicated: the harder-evidenced error-correction result. It is a reward-learning signal in an RL frame, not perceptual inference; Friston recasts dopamine as precision of prediction errors — a reinterpretation, not the mainstream reading. RPE ≠ evidence for FEP.

**AI reception.** Variational free energy = negative ELBO; VAEs (Kingma & Welling 2013/14) optimise exactly this objective — so FEP-as-loss-function is unremarkable in ML; the distinctive claim is the active-inference mechanism (planning as inference, expected free energy). Active inference in ML is a growing niche (IWAI, pymdp); Friston joined VERSES AI as Chief Scientist (Dec 2022) — commercially promoted, not mainstream-adopted.

**Person-page facts.** b. 12 July 1959, York; Cambridge natural sciences; psychiatry training; schizophrenia research origin (dysconnection hypothesis, w/ Peter Liddle). Scientific Director, Wellcome Centre for Human Neuroimaging (FIL), UCL. Earlier towering contributions — SPM (the standard fMRI/PET analysis framework), VBM, DCM — drive his citation standing, not FEP. ~20th most-cited living scientist, >260k citations; safe phrasing "among the most-cited neuroscientists alive." FRS 2006.

**Reception status.** Predictive processing/Bayesian-brain is a productive, common framework; SPM/DCM universally adopted infrastructure. FEP itself sits in a polarised middle: an enthusiastic community (computational psychiatry, active inference, Clark/Hohwy in philosophy), a larger body of working neuroscientists who ignore it as too abstract to constrain experiments, and an articulate critical literature converging on: math sound but over-interpreted, principle not testable, empirical weight rests on process theories whose evidence remains mixed.

---

## Flags for the survey post (accuracy)

1. **Edelman Nobel sentence.** The post says he "won a Nobel for showing that the immune system meets a novel antigen not by templating an antibody to fit it but by selecting from a pre-existing repertoire." The 1972 prize (shared, Porter) was for the *chemical structure of antibodies*. Clonal selection is Burnet's theory (Nobel 1960), which Edelman's structural work supported and which he then transposed. The post's sentence over-credits — reword.
2. **Laminar recordings sentence.** The post states "laminar recordings tell the descending predictions from the ascending errors by cortical layer" as clean evidence. The literature is mixed (contra-findings in rodent mPFC, *PLOS Biology* 2020). Soften to suggestive, or lean on repetition suppression + MMN and drop the laminar claim.

## Round conclusions (for the build)

- Baars-first call confirmed: undisputed originator, cordial relationship, Dehaene's contribution is mechanism + evidence. Dehaene external-linked on Baars page and in the subject entry.
- Bonus connection: Baars worked at Edelman's Neurosciences Institute — the two on-site persons connect directly.
- The three models' honest field standings differ sharply and the entries should say so: TNGS largely historical (absorbed unbranded), GWT/GNW live and leading but bruised (Cogitate, no-report), FEP polarised (principle unfalsifiable-by-design, process theories mixed).
- AI-reception one-liners per entry: LTH rhyme informal only (Edelman); Bengio consciousness prior + workspace transformers verified (GWT); ELBO equivalence + active inference niche (Friston).
