import express from 'express';
import helmet from 'helmet';
import { env } from './env.js';
import { paypalRouter } from './routes/paypal.js';

export const app = express();
app.use(helmet());
app.use(express.json({ limit: '10kb' }));

app.use('/api/paypal', paypalRouter);

app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    system: 'UMAJA-OMEGA-v2.1',
    config: { architect: `${env.SPLIT_ARCHITECT}%`, justice: `${env.SPLIT_JUSTICE}%` }
  });
});
