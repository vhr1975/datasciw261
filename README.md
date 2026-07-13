# Machine Learning at Scale: Distributed Systems for Real Data

This is a hands-on portfolio of distributed ML work completed in 2022 at UC Berkeley. The core challenge: **How do you train and run ML models when your data is too big for one computer?**

## The Problem I Solved

In the real world, companies don't process data on laptops. Netflix trains on billions of user interactions. Twitter classifies spam across trillions of tweets. Google searches an index built from the entire web. This coursework is my proof that I understand how to build systems that work at that scale — not by calling a library function, but by actually implementing the parallel algorithms that make it work.

Each assignment was executed on a live cloud cluster (Google Cloud Dataproc), not simulated on a single machine. That matters. You'll see actual job logs, timing curves, and working code.

## What This Taught Me (In Plain English)

**Homework 1: Breaking Work Into Pieces**
The simplest problem: count word frequency in a large text file. On a laptop, you read the whole file once. On a cluster, you split the file across 4, 8, or 32 machines, each counts their own chunk, then combine the results.

The insight: Some tasks scale perfectly (2× machines = 2× faster). Others don't (overhead of coordination eats into gains). I measured this directly — timing curves show where the sweet spot is.

**Homework 2: Training a Classifier in Parallel**
I built a spam detector for Enron emails using Naive Bayes — a standard ML algorithm. But instead of training on one machine, I designed a data pipeline that:
1. Splits the corpus across parallel workers
2. Each worker processes their chunk independently  
3. Results are recombined correctly (the hard part — data alignment matters)

Result: 85% accuracy, 88% F-score. Job logs show it ran on a live YARN cluster — this isn't pseudocode.

**Homework 3: Finding Similar Words at Scale**
Built a synonym detector that compares 100,000+ word pairs by measuring similarity (cosine, Jaccard). Instead of comparing all pairs on one machine (infeasible), I structured the data as inverted indices and distributed the computation across Spark workers.

## Why This Matters for ML Work

Most data science bootcamps teach you how to use libraries: scikit-learn, TensorFlow, pandas. Those are important. But they gloss over the hard part: **what happens when you have 100 GB of data, not 1 GB? What breaks? How do you fix it?**

This work answers those questions with code. I didn't just learn MapReduce theory — I shipped working implementations that handle edge cases (data skew, fault tolerance, memory constraints). I measured where parallelism helps and where it hurts.

That's the difference between a data scientist who can prototype and one who can scale.

## What You're Seeing Here

- **Three complete homework notebooks** with full code and results
- **Live cluster execution** (not local simulation) — actual job logs from Google Cloud
- **From scratch implementations** of algorithms, not library calls
- **Concrete metrics**: timing benchmarks, accuracy scores, efficiency curves
- **Honest timeline**: 2022 coursework, presented fresh in 2026 (no backdating)

## Technical Stack

Python 3.8 · Hadoop 3.2.3 (Streaming) · PySpark · Google Cloud Dataproc · HDFS/GCS

## About the Code Comments

Some TODO comments appear in the HW2 mapper/reducer scripts — these were part of the assignment template provided by the course instructors. The implementations are complete and tested; the comments were preserved as-is from submission.

## How This Prepared Me for ML Work

This coursework built the foundation for understanding how modern ML systems actually work:

- **Scalability first**: Every design decision trades off accuracy, speed, and cost
- **Systems thinking**: ML models are 10% of the work; infrastructure is the other 90%
- **Debugging at scale**: When something breaks on 32 machines, it's not the same as debugging on 1
- **Data pipelines**: How data flows through parallel systems, where it gets stuck, why it matters

These are the skills that separate "works on my laptop" from "works in production."
