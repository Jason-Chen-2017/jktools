import { client } from "@gradio/client";

const app = await client("https://modelscope.cn/api/v1/studio/qwen/Qwen-14B-Chat-Demo/gradio/");
const result = await app.predict(0, [
    "Howdy!", // string  in 'Input' Textbox component
    "null", // any (any valid json) in 'Qwen-14B-Chat' Chatbot component
]);

console.log(result.data);
