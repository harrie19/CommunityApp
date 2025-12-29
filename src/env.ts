import { z } from 'zod';
import dotenv from 'dotenv';
dotenv.config();

const envSchema = z.object({
  PORT: z.coerce.number().default(3000),
  SPLIT_ARCHITECT: z.coerce.number().min(0).max(100).default(81),
  SPLIT_JUSTICE: z.coerce.number().min(0).max(100).default(19),
}).refine((data) => data.SPLIT_ARCHITECT + data.SPLIT_JUSTICE === 100, {
  message: "Huqúqu'lláh-Protokoll verletzt: Summe muss 100 sein!"
});

export const env = envSchema.parse(process.env);
