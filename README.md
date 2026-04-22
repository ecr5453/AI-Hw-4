# LLM API Experiment

## Overview
This project demonstrates how to interact with a Large Language Model (LLM) using Python code instead of a web interface. The OpenAI Python SDK was used to send prompts programmatically and retrieve responses.

## Code Description
The script sends multiple prompts to the model using the OpenAI API and prints the responses to the console. This shows how LLMs can be used at scale through code rather than manual input.

## Prompts Used
1. List 3 benefits of regular exercise.
2. Explain the benefits of exercise to someone who hates working out in a friendly tone.

## Expected Behavior
The model should adapt its response based on the prompt:
- The first prompt should produce a short, structured list.
- The second prompt should produce a more conversational and persuasive explanation.

## Observations
The output of the first prompt just listed three benefits with non additional explanation. On the other hand, the second prompt had an easy to understand, conversational tone explaining the benefits of exercise. 

## Notes on Execution
When running the script, the following error was encountered: "insufficient quota" error, which indicates that the request reached the API but could not be processed due to account limitations. 
