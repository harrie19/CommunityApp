import express from 'express';
import { env } from './env.js';

export const app = express();

app.use(express.json());

app.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp:  new Date().toISOString(),
    config: {
      SPLIT_A: env.SPLIT_A,
      SPLIT_B: env.SPLIT_B
    }
  });
});
