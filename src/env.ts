import { z } from 'zod';
import dotenv from 'dotenv';

dotenv.config();

const envSchema = z.object({
  SPLIT_A: z.string().default('81').transform(Number),
  SPLIT_B: z.string().default('19').transform(Number),
  PORT: z.string().default('3000').transform(Number),
});

export const env = envSchema.parse(process.env);
