import { Router } from 'express';
import { env } from '../env.js';
import crypto from 'crypto';

export const paypalRouter = Router();

paypalRouter.post('/webhook', (req, res) => {
  const signature = req.headers['paypal-transmission-sig'];
  // TODO: Hier HMAC-Verifizierung mit env.PAYPAL_WEBHOOK_ID implementieren
  
  const { amount, currency, id } = req.body;
  const archAmount = (amount * env.SPLIT_ARCHITECT) / 100;
  const justAmount = (amount * env.SPLIT_JUSTICE) / 100;

  console.log(`⚖️  Split für ${id}: ${archAmount}${currency} (A) / ${justAmount}${currency} (J)`);
  res.status(200).json({ status: 'processed', architect: archAmount, justice: justAmount });
});
