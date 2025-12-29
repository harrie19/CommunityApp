import { app } from './app.js';
import { env } from './env.js';

app.listen(env.PORT, () => {
  console.log(`🛡️  UMAJA-OMEGA AKTIV AUF PORT ${env.PORT}`);
  console.log(`⚖️  SPLIT-RESONANZ: ${env.SPLIT_ARCHITECT}/${env.SPLIT_JUSTICE}`);
});
