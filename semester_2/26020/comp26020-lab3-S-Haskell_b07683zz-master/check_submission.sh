#!/bin/bash
cat submission.hs > check_submission_temp_file.hs
cat tester.hs >> check_submission_temp_file.hs
ghc check_submission_temp_file.hs
./check_submission_temp_file
