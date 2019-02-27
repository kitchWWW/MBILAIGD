#!/bin/bash


rm -r notes/5_41/*
clingo 3 notes_generator.lp notes_general.lp notes_prettify.py
