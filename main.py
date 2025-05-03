from fastapi import FastAPI
import random

app = FastAPI()


success_ideas = [
    "Launch your own niche blog and monetize with ads & affiliates",
    "Design and sell merch through print-on-demand platforms",
    "Create and sell Notion templates or productivity tools",
    "Start a newsletter and monetize with premium subscriptions",
    "Build Shopify stores for e-commerce startups",
    "Host paid online workshops or webinars",
    "Offer conversion-focused landing page design",
    "Build & sell mobile apps or micro-SaaS tools",
    "Provide SEO or content marketing services",
    "Monetize your skills with online coaching or consulting"
]

wealth_wisdom = [
    "Success is not in what you have, but who you become. – Eric Thomas",
    "Build assets, not just income. Let your money outwork you. – Anonymous",
    "Wealth isn’t about having a lot of money, it’s about having options. – Chris Rock",
    "Discipline is the bridge between goals and financial freedom. – Jim Rohn",
    "Focus on building systems, not just hustle. – Naval Ravikant",
    "Financial freedom is freedom from fear. – Robert Kiyosaki",
    "Don't save what is left after spending, spend what is left after saving. – Warren Buffett",
    "You don’t have to be rich to start, but you have to start to be rich. – Zig Ziglar"
]


@app.get("/success_ideas")
def get_success_ideas(apiPassword:str):
    """Return a random success_ideas idea"""
    if apiPassword != "123":
        return {"Error": "Invalid api Password"}
    return {"success_ideas": random.choice(success_ideas)}

@app.get("/wealth_wisdom")
def get_wealth_wisdom(apiPassword:str):
    """Return a random wealth_wisdom idea"""
    if apiPassword != "123":
        return {"Error": "Invalid api Password"}
    return {"wealth_wisdom": random.choice(wealth_wisdom)}