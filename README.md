# Machine Learning at Scale: Distributed Systems for Real Data

Hands-on coursework from 2022 at UC Berkeley. Core problem: how do you train ML models when data won't fit on a single machine?

## The Work

Real-world ML systems process data on clusters, not laptops. Netflix trains on billions of user interactions. Twitter classifies spam at scale. Google indexes the web. This coursework is proof I understand how to build that kind of system. Not theory or library calls. Actually implementing the parallel algorithms that make it work.

Each assignment ran on a live cloud cluster (Google Cloud Dataproc). Not simulation. Actual job logs, timing curves, working code.

## What I Built

**HW1: Parallel Word Count**
Simplest distributed problem. Count word frequency in a large text file. Single machine reads the whole thing once. On a cluster, split the file across 4, 8, or 32 machines, each counts their chunk, combine results.

Key insight: perfect scaling (2x machines = 2x faster) only happens up to a point. Coordination overhead kills gains beyond that. Measured this directly. Timing curves show the crossover.

**HW2: Training a Classifier in Parallel**
Built a spam detector for Enron emails using Naive Bayes. Instead of training on one machine, designed a data pipeline that splits the corpus across parallel workers, processes chunks independently, and recombines results correctly. Last part is the hard part. Data alignment matters.

Results: 85% accuracy, 88% F-score. Job logs prove it ran on a live YARN cluster. Not pseudocode.

**HW3: Similarity Search at Scale**
Built a synonym detector comparing 100,000+ word pairs by similarity (cosine, Jaccard). Can't compare all pairs on one machine. Instead structured the data as inverted indices and distributed computation across Spark workers.

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
