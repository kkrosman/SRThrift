﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;
using log4net;

namespace BankingNode
{
    class BalanceManager
    {
        private readonly ILog logerr = LogManager.GetLogger(MethodBase.GetCurrentMethod().DeclaringType);
        public Int64 Balance { set; get; }
        private Int64 counter = 0;
        private object _lock = new object();
        public List<TransferData> Transacitons = new List<TransferData>();
        /// <summary>
        /// Dostęp do listy tranzakcji
        /// </summary>
        public List<SRBanking.ThriftInterface.TransferData> BaseTransactions
        {
            get
            {
                List<SRBanking.ThriftInterface.TransferData> t = new List<SRBanking.ThriftInterface.TransferData>();
                foreach (TransferData d in Transacitons)
                {
                    t.Add(d.ToBase());
                }
                return t;
            }
        }
        /// <summary>
        /// 
        /// </summary>
        /// <returns> Zwraca nowy numer transakcji</returns>
        public TransferID generateTransactionID()
        {
            TransferID t = new TransferID();
            lock (_lock)
            {
                t.Counter = counter++;
                t.Sender = ConfigLoader.Instance.ConfigGetSelfId();
            }
            return t;
        }
        /// <summary>
        /// Sprawdza czy możliwe jest dokonanie tranzakcji tego typu
        /// </summary>
        /// <param name="transaction"></param>
        public void checkTransfer(TransferData transaction)
        {
            if (Balance - transaction.Value < 0)
            {
                throw new SRBanking.ThriftInterface.NotEnoughMoney();
            }
        }
        /// <summary>
        /// 
        /// </summary>
        /// <param name="transaction"></param>
        public void CommitTransfer(TransferData transaction)
        {
            logerr.Info(transaction.TransferID.Sender.ToString() + " vs " + transaction.Receiver.ToString());
            if (transaction.TransferID.Sender == transaction.Receiver)
                return;

            if (transaction.TransferID.Sender == ConfigLoader.Instance.ConfigGetSelfId())
            {

                if (Balance - transaction.Value < 0)
                {

                    throw new SRBanking.ThriftInterface.NotEnoughMoney();
                }
                //Transacitons.Add(transaction);

                lock (_lock)
                {
                    Balance -= transaction.Value;
                }

            }
            else
            {
                
                lock (_lock)
                {
                    if (!Transacitons.Contains(transaction))
                    {
                        Transacitons.Add(transaction);
                        Balance += transaction.Value;
                    }
                }

            }
            
        }
    }
}
