import { app } from './app.js';
import { env } from './env.js';
app.listen(env.PORT, () => {
  console.log(`🛡️ UMAJA-CORE AKTIV AUF PORT ${env.PORT}`);
  console.log(`⚖️ SPLIT: ${env.SPLIT_A}/${env.SPLIT_B}`);
});
