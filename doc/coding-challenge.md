# eBay Ads - Ams Coding Challenge

### Welcome fellow coder!

![Fellow Coder](https://media.giphy.com/media/OIEhvGRByVrHO/giphy.gif)

<br/>

#### Introduction

---

You have chosen to undertake the Ebay Ads's Coding Challenge.

This is a challenge and not a test! It is not about passing or failing, but rather about us giving you a clean canvas that you can use to demonstrate how passionate you are about coding. Thus, go forth **champion** and prove to us that you have what it takes to survive the every day life as a code wielding bug slayer!

Are you ready?

![Yes Sir](https://media.giphy.com/media/RavXJWRY3veEw/giphy.gif)

If that is your response, or something similar, we should probably get down to the details!

<br/>

#### Getting started:

---

To get started, please create a new public repo where you can commit your code. Remember to make regular commits se we can see how you break down your functionality! Once you have finished the challenge or you have ran out of time, please send us a link to your repo.

<br/>

#### Before you start

---

A few things that you should know before you start:

- Please makes sure that read through the entire challenge before starting.
- You need to use a personal email to get twitter Api free basic access.
- Please do frequent and well commented commits.
- Commenting your code is not mandatory, but help us review.
- It does not have to be the prettiest solution, so much as clever.
- Please tag the final commit of each phase completed.

<br/>
Back-End requirements:

- You can implement the solution using any languages that you are familiar, but Scala or Java would be preferable
- You can use a in-memory key-value storage to sync your aggregations, use docker-compose if needed.
- Each phase of the project will count as an entire feature delivered on a sprint.
- Use your highest professional standards, so we can evaluate you at your best.
- Your code should work locally in any machine with average to above configuration

<br/>

#### Challenge description:

---

###### Background

We would like to compare how many messages per period the top trends subjects at twitter have, to do that you need to connect with their Streaming API (free-version)

**<span style="color: red;">NOTE!</span>**:
We're aware that Twitter has closed its free API as of May 1, 2023. But you can use PubNub streaming service for getting tweets. We also know that they're 3-4 months behind so not to worry.
You'll need to consume tweets from this stream API via your consumer, filter them and aggregate them for your needs. Simple, right? :)

You can find some useful resources below:
- PubNub Demo page for some stream pipes: https://www.pubnub.com/demos/real-time-data-streaming/?show=demo
- PubNub JAVA SDK: https://www.pubnub.com/docs/sdks/java
- PubNub Python SDK: https://www.pubnub.com/docs/sdks/python
- PubNub Scala SDK has been deprecated but then again you can always use JAVA SDK in place.
- **<span style="color: red;">Important</span>** PubNub Subscriber Key for Twitter API Producer: **sub-c-d00e0d32-66ac-4628-aa65-a42a1f0c493b**
- **<span style="color: red;">Important</span>** PubNub Consumer Channel for Twitter API Producer: **pubnub-twitter**
- **<span style="color: red;">Important</span>** You must define a UUID for your consumer but you can define it anything you want. (eg; MyTwitterConsumer)

<br/>

###### Phase 1:

Create a client that connects with PubNub.

###### Phase 2:

You should implement a client able to consume the 3 (default) top trends in the Netherlands (default) and make it configurable on your API.

###### Phase 3:

You should implement a client that connects with Twitter stream and calculates (on your consumer) how many tweets we have every 1, 5 and 10 minutes for a trend topic. Make it configurable on your Rest API.

###### Phase 4:

You should sync these aggregations on a key-value storage using the time period + the time leap as a key and a payload as value having information about the trend-topic, number of tweets and any other information that looks important to you.

<br/>

#### Side notes:

---

- Kudos if you leave the project in working order.
- Kudos if you have unit test coverage.
- Kudos if you have well structured and clean code.
- Kudos if you have documentation on how to run project.
- Kudos if you use some sort of state management.

<br/>

#### Finally:

After we had time to review your awesome solution we will get back to you.

![You Can Do IT!](https://media.giphy.com/media/yoJC2K6rCzwNY2EngA/giphy.gif)

##### Good luck and have fun!

