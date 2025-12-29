import express from 'express';
import helmet from 'helmet';
import { env } from './env.js';

export const app = express();
app.use(helmet());
app.use(express.json({ limit: '10kb' }));

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    system: 'UMAJA-v2.1',
    timestamp: new Date().toISOString(),
    splitConfig: { architect: env.SPLIT_ARCHITECT, justice: env.SPLIT_JUSTICE }
  });
});

app.use((err: Error, req: any, res: any, next: any) => {
  console.error('UMAJA Error:', err.message);
  res.status(500).json({ error: 'Internal system error' });
});
