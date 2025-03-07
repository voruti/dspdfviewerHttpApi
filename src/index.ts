import express, { Express, Request, Response } from "express";

const app: Express = express();

app.get("/", (_: Request, response: Response) => {
    response.send("Hello World");
});

app.listen(3000);
