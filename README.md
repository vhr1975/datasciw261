# Machine Learning at Scale: Distributed Systems for Real Data

Completed coursework from UC Berkeley MIDS W261 (Fall 2022). Grade: A. 

Core problem: how do you train ML models when data won't fit on a single machine? This course taught me to implement distributed algorithms from scratch, not just use libraries. MapReduce. Spark. Custom partitioners. Live cluster execution. Real failure modes and how to debug them.

## The Work

Real-world ML systems process data on clusters, not laptops. Companies like Netflix, Twitter, and Google tackle this category of problem at scale. This coursework is proof I understand how to approach that challenge. Not theory or library calls. Actually implementing the parallel algorithms that make it work.

Each assignment ran on a live cloud cluster (Google Cloud Dataproc). Not simulation. Actual job logs, timing curves, working code.

## What I Built

**HW1: Parallel Word Count**
Simplest distributed problem. Count word frequency in a large text file. Single machine reads the whole thing once. On a cluster, split the file across 4, 8, or 32 machines, each counts their chunk, combine results.

Key insight: perfect scaling (2x machines = 2x faster) only happens up to a point. Coordination overhead kills gains beyond that. Measured this directly. Timing curves show the crossover.

**HW2: Training a Classifier in Parallel**
Built custom mapper/reducer scripts to train a Naive Bayes spam classifier on the Enron corpus using Hadoop Streaming. Implemented the order-inversion pattern with a custom KeyFieldBasedPartitioner to handle data skew across parallel workers. Training phase executed on a live YARN cluster with actual job logs. Algorithm produces correct conditional probabilities matching expected results. Encountered failure during final output phase, a real lesson in why distributed systems require robustness at every layer.

**HW3: Similarity Search at Scale**
Implemented co-occurrence analysis and similarity metrics (Cosine, Jaccard, Overlap, Dice) in PySpark on GCP Dataproc. Designed inverted index structures to avoid O(n²) all-pairs comparison. The notebooks here reflect the learning process, including distributed systems challenges encountered during development.

## Why This Matters

Most data science training teaches libraries: scikit-learn, TensorFlow, pandas. Those are tools. What they skip is the real bottleneck: what happens when you have 100 GB of data, not 1 GB? What breaks? How do you fix it?

This work answers those questions. I didn't just learn MapReduce theory. I shipped working implementations that handle real edge cases. Data skew. Fault tolerance. Memory constraints. I measured where parallelism helps and where it becomes overhead.

That gap. Between building a prototype and shipping at scale. That's what separates the two.

## What's Here

Three complete homework notebooks with full code and outputs. Live cluster execution (not local). Actual job logs from Google Cloud. Implementations built from scratch, not library wrappers. Concrete metrics: timing benchmarks, accuracy scores, efficiency curves. Timeline is honest. 2022 coursework, presented in 2026.

## Technical Stack

Python 3.8 | Hadoop 3.2.3 (Streaming) | PySpark | Google Cloud Dataproc | HDFS/GCS

## Code Comments

Some TODO comments appear in HW2 mapper/reducer scripts. These came from the assignment template. Implementations are complete and tested. Comments preserved as submitted.

## Systems Skills This Built

Scalability first. Every design decision trades accuracy, speed, cost. ML models are 10% of production systems. Infrastructure is the other 90%. Debugging at scale is different than debugging locally. When something breaks on 32 machines, root cause analysis changes. Data pipelines matter. How data flows through parallel systems. Where it gets stuck. Why it matters.

Skills that separate prototype from production.
