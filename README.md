# UC Berkeley Data Science W261: Machine Learning at Scale

> Distributed ML implemented from scratch on Hadoop MapReduce and Spark — not library calls, the actual parallel algorithms.

## What This Is

Coursework from UC Berkeley's MIDS W261 (Machine Learning at Scale), covering distributed
Naive Bayes, MapReduce design patterns, and Spark-based similarity search at corpus scale.
Each homework was executed on a live GCP Dataproc cluster, not simulated locally.

## What You'll Learn

- Why word counting is "embarrassingly parallel" — and where that stops being true (see HW1
  timing benchmarks across 2–32-way parallelism)
- Distributed Naive Bayes: training, smoothing, and evaluation via Hadoop Streaming mappers/reducers
- The order-inversion pattern via a custom `KeyFieldBasedPartitioner` and `KeyFieldBasedComparator`
- Synonym detection in Spark using stripes vs. pairs, inverted indices, and four similarity
  metrics (Cosine, Jaccard, Overlap, Dice) at scale

## Homework Breakdown

**HW1 — Embarrassingly Parallel Word Count**
Bash + Python MapReduce word count on *Alice in Wonderland*, benchmarked across 2/4/8/16/32-way
parallelism with `%%timeit`. Runtime increases past the optimal parallelism point — the curve
itself is the finding.

**HW2 — Distributed Naive Bayes (Hadoop Streaming)**
Trained and evaluated a multinomial Naive Bayes spam classifier on the Enron corpus using
custom mapper/reducer scripts. Implements the order-inversion pattern with a custom
`KeyFieldBasedPartitioner`. Smoothed model: 0.85 accuracy, 0.88 F-score, executed on a live
YARN cluster (job logs included).

**HW3 — Synonym Detection at Scale (Spark)**
Built co-occurrence stripes and an inverted index in PySpark on GCP Dataproc, then ranked word
pairs by Cosine/Jaccard/Overlap/Dice similarity across a full corpus run.

## Technologies Used

Python 3.8, Hadoop 3.2.3 (Streaming), PySpark, GCP Dataproc, HDFS/GCS

## Note on Scope

This repo previously described only HW1–3 at a high level without the underlying notebooks.
The homeworks above are individually authored and independently executed; a Section 2 Group 3
final project also exists but is not included here as it reflects team-planning work rather
than completed individual implementation.

## Reflection

This coursework is the direct precedent for the distributed-systems and evaluation thinking
now applied across `ai-operating-system`, `edge-ai-agent-lab`, and `rag-evaluation-lab` —
the shift from "call a pretrained model well" to "understand what's happening under the hood
when you parallelize a calculation."
