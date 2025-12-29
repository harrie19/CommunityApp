import { Router } from 'express';
import { env } from '../env.js';

export const paypalRouter = Router();

paypalRouter.post('/webhook', async (req, res) => {
  try {
    const { resource } = req.body;
    const amount = parseFloat(resource.amount.value);
    const currency = resource.amount.currency_code;
    
    const archAmount = (amount * env.SPLIT_ARCHITECT) / 100;
    const justAmount = (amount * env.SPLIT_JUSTICE) / 100;

    console.log(`⚖️  TRANS-ID: ${resource.id} | SPLIT: ${archAmount} (A) / ${justAmount} (J)`);
    res.status(200).json({ status: 'processed' });
  } catch (e) {
    res.status(400).send('Invalid Webhook Data');
  }
});
