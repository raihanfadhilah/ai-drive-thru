Both tasks will be part of your daily job. Please demonstrate you have the skills required for this job. Feel free to choose any of these two challenges. Finally, we would like to know your reasoning behind your choice.

If you have any questions you can contact Maurice by email: maurice@voxai.tech.

# 1: Show-Us-Your-RAG-Skillz demo
The demo menu is attached (menu.json). In real life, this menu is much bigger with more options. If you're interested. Hence, in order to save on tokens for the prompt, we want to use RAG.

## Consider the following questions being asked:

- Hi, do you have cola?
- Hi I want to have a Fire Zinger Stacker without sauce and a cola
- Give me a Veggie Tender, medium, with salad
- Give me an orange chocolate milkshake, medium
- Give me the gluten free burger options
- How many calories does the Colonel have?
- Can I get a Whopper?

## Requirements:

- Total prompt generation time: < 50ms.
- The vector db should be able to maintain/update (so compiling anything is out of the question)

## General remarks:

- Db in memory is fine.
- LLM is not required for demo. If you do, it's appreciated, then please demonstrate Mistral or other open source model locally.
- Write like you would normally write. Using tools like copilot is totally ok, even encouraged
- Your demo does not have to be complete before entry. If it is not, please walk us through your next steps.
- Don’t forget the readme

## Evaluation:
- Your code
- Speed of query
- Accuracy
- Scalability / Production readyness
- Your ideas to make it faster or improvements you thought of
- Demo completeness & presentation during our call

Please send this in a repo or gist in advance so we can review your code, you can add the following users with view permissions: zazpie, vin136, xapss

**Deadline: Monday Feb 26, 11.30AM GMT+1 (Amsterdam time)**.

# 2: Automate-The-World-With-Agentz demo

We are making a ton of integrations with third party APIs: Point Of Sale (POS) systems, Headset base stations, Call center software; and many others.
We are not going to be a traditional company with a backend team that creates all these integrations manually. Instead, we are going to use agents.
Agents are typically meant for prototyping. We are going to use them in production. This is impossible, right? Prove us wrong.

Create a stable integration for the following POS (Aloha NCR POS). Attached is a sandbox, you can do anything with this so don’t worry about breaking anything.

Everything needed to make calls — including necessary credentials — is included in this downloadable Postman collection (sandbox-collection.json). It’s pre-populated and ready-to-use. Simply load the collection into Postman, review or modify the request headers and body, then get real responses back from our safely sandboxed APIs.

So, the postman collection has everything. We don’t need most of it. Optimize what you use for your calls.

## There will be “only” 2 tasks required in this demo:

1. Order something
2. Request for checkout, give the total.

## General remarks:

- Doing this right will require you to think through multiple steps. As a hint, you will need to open up an order first.
- There are no time requirements for this job. This is run in asynchronous mode so it can take several seconds to complete: no worries.
- Write like you would normally write. Using tools like copilot is totally ok, even encouraged
- Your demo does not have to be complete before entry. If it is not, please walk us through your next steps.
- Don’t forget the readme
- You can use any open source LLM that you think works best
- You won’t need it, but if you want more background info on the API, you can find it at https://developer.ncr.com/portals/dev-portal/getting-started

## Evaluation:

- Your code
- Stability
- Production ready code
- Scalability
- Your ideas to make it faster or improvements you thought of
- Demo completeness & presentation during our call

Please send this in a repo or gist in advance so we can review your code, you can add the following users with view permissions: zazpie, vin136, xapss

**Deadline: Monday Feb 26, 11.30AM GMT+1 (Amsterdam time).**