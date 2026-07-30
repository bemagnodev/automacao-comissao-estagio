# IC/UFRJ Internship Committee Automation

![Status](https://img.shields.io/badge/status-completed-brightgreen?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![PDFPlumber](https://img.shields.io/badge/PDFPlumber-4A5568?style=for-the-badge)

---

## Overview

Python automation tool developed to optimize the document verification workflow of the Internship Committee at the Institute of Computing (IC) at the Federal University of Rio de Janeiro (UFRJ).

The goal is to reduce manual work and speed up the preliminary analysis of student internship requests, as part of **InovaProcess**, an extension project focused on process improvement at the Institute of Computing.

*This repository is a fork of the [original project](https://github.com/Inova-Process/automacao-comissao-estagio), where I am an active contributor.*

## The Problem

The current internship request workflow involves manual document checking, which can be slow and prone to bottlenecks. The main challenges include:

- **Strict deadlines:** students must submit internship documentation within specific deadlines.
- **Manual verification:** the committee needs to review each document manually.
- **Process bottlenecks:** manual checks can delay the preliminary analysis of student requests.

## The Solution (MVP)

The first version of the tool is an automation script that performs a preliminary analysis of student academic documents and returns a validation result based on predefined business rules.

The MVP currently checks whether the student:

- has a cumulative academic coefficient (CRA) of at least 6.0;
- has completed all mandatory credits up to the 4th academic period;
- is within the maximum 14-semester course completion limit;
- has completed at least 160 hours of extension activities.

## My Role and Contributions

As one of the developers of the project, my current responsibilities include:

- developing the main automation script in Python;
- implementing business rules for extracting and validating data from UFRJ academic records;
- researching and selecting libraries for PDF parsing and document processing;
- contributing to the structure of an automation workflow for a real administrative process at the Institute of Computing.

## Contributors

- [Bernardo Magno](https://github.com/bemagnodev)
- [Felipe Rivetti](https://github.com/feliperivetti)
