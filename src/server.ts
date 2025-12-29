import { app } from './app.js';
import { env } from './env.js';

const PORT = env.PORT;

app.listen(PORT, () => {
  console.log(`🚀 UMAJA-Backend läuft auf Port ${PORT}`);
  console.log(`📊 SPLIT_A: ${env.SPLIT_A}, SPLIT_B: ${env.SPLIT_B}`);
  console.log(`🏥 Health-Check: http://localhost:${PORT}/health`);
});
