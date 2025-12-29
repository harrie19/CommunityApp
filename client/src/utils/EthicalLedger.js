class EthicalLedger {
  constructor() { 
    this.transactions = this.loadFromStorage(); 
    this.socialImpactWallet = this.calculateSocialTotal();
  }

  loadFromStorage() {
    try { return JSON.parse(localStorage.getItem('umaja_ledger') || '[]'); } 
    catch { return []; }
  }

  calculateSocialTotal() {
    return this.transactions.reduce((acc, tx) => acc + (tx.totalRevenue * 0.19), 0);
  }

  recordRevenue(amount, source) {
    const timestamp = Date.now();
    const socialShare = amount * 0.19; 
    const operational = amount * 0.81;

    this.socialImpactWallet += socialShare;

    const transaction = {
      id: `${timestamp}-${source}`,
      timestamp,
      totalRevenue: amount,
      socialShare,
      operational,
      source
    };

    this.transactions.push(transaction);
    localStorage.setItem('umaja_ledger', JSON.stringify(this.transactions)); // PERSISTENCE

    return { operational, social: socialShare };
  }

  canTrade(requestedAmount) {
    const funds = this.transactions.reduce((acc, tx) => acc + (tx.totalRevenue * 0.81), 0);
    return requestedAmount <= funds;
  }
}

export default new EthicalLedger();
