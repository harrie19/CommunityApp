import { z } from 'zod';
import dotenv from 'dotenv';
dotenv.config();
const schema = z.object({
  PORT: z.string().default('3000').transform(Number),
  SPLIT_A: z.string().default('81').transform(Number),
  SPLIT_B: z.string().default('19').transform(Number)
});
export const env = schema.parse(process.env);
if (env.SPLIT_A + env.SPLIT_B !== 100) {
  console.error("❌ ERROR: Split ungültig!");
  process.exit(1);
}
