#!/usr/bin/env Rscript
args <- commandArgs(TRUE)
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager", repos = "http://cran.us.r-project.org")

#BiocManager::install("DiffLogo")
#library(DiffLogo)

listNetze <- list.files("D:/Masterarbeit/ZinkFinger/Predictions/", full.names=TRUE)
DBDs <- list.files("D:/Masterarbeit/ZinkFinger/DBDsALL_new")
ListPWMS <- list.files('D:/Masterarbeit/ZinkFinger/PWMSaufgefuellt')
TestDatenDBD <- as.matrix(read.csv('D:/Masterarbeit/ZinkFinger/DBDTestDaten5.csv', sep='\n'))

TestDatenDBD[1]

for (i in 1:length(listNetze)){
  if (grepl("prediction007", listNetze[i]) == TRUE){
    KL_DIV <- read.table(paste(listNetze[i],'/kl_divergencen.tsv', sep=''))
    for (k in 1:length(DBDs)){
      ListMotivIDs <- list.files(paste("D:/Masterarbeit/ZinkFinger/DBDsALL_new/",DBDs[k], sep=''))
      ausgabename = paste(paste(listNetze[i],"/pdfs2/",sep=""),paste(strsplit(DBDs[k],"/")[1][[1]][1],".pdf",sep=""),sep="")
      for (MotivID in 1:length(ListMotivIDs)){
        for (pwm in 1:length(ListPWMS)){
          if (ListMotivIDs[MotivID] == ListPWMS[pwm]){
            if (MotivID == 1){
              list <- KL_DIV[pwm, 1]
            }else{
              list[[MotivID]] <- KL_DIV[pwm, 1]
            }
          }
        }
        namen = strsplit(ListMotivIDs[1],'_')[[1]][1]
        print(strsplit(ListMotivIDs[2],'_')[[1]][1])
        if (length(ListMotivIDs)>1){
          for (zaehler in 2:length(ListMotivIDs)){
            namen[zaehler] <- strsplit(ListMotivIDs[zaehler],'_')[[1]][1]
          }
        }
        print(length(namen))
        pdf(file = ausgabename, width = 12, height = 6)
        plot(list, xaxt='n', xlab="", ylab="KL_DIVERGENCE", main=DBDs[k])
        axis(1, at=1:length(ListMotivIDs), labels=namen, las=2, cex.axis=0.8)
        dev.off()
      }
    }
  }
}


#TESTDATE
for (i in 1:length(listNetze)){
  if (grepl("prediction007", listNetze[i]) == TRUE){
    KL_DIV <- read.table(paste(listNetze[i],'/kl_divergencen.tsv', sep=''))
    for (k in 1:length(DBDs)){
      for (DBDSSS in 1:length(TestDatenDBD)){
        if (DBDs[k] == TestDatenDBD[DBDSSS]){
          ListMotivIDs <- list.files(paste("D:/Masterarbeit/ZinkFinger/DBDsALL_new/",DBDs[k], sep=''))
          ausgabename = paste(paste(listNetze[i],"/pdfs3/",sep=""),paste(strsplit(DBDs[k],"/")[1][[1]][1],".pdf",sep=""),sep="")
          for (MotivID in 1:length(ListMotivIDs)){
            for (pwm in 1:length(ListPWMS)){
              if (ListMotivIDs[MotivID] == ListPWMS[pwm]){
                if (MotivID == 1){
                  list <- KL_DIV[pwm, 1]
                }else{
                  list[[MotivID]] <- KL_DIV[pwm, 1]
                }
              }
            }
            namen = strsplit(ListMotivIDs[1],'_')[[1]][1]
            print(strsplit(ListMotivIDs[2],'_')[[1]][1])
            if (length(ListMotivIDs)>1){
              for (zaehler in 2:length(ListMotivIDs)){
                namen[zaehler] <- strsplit(ListMotivIDs[zaehler],'_')[[1]][1]
              }
            }
            print(length(namen))
            pdf(file = ausgabename, width = 12, height = 6)
            plot(list, xaxt='n', xlab="", ylab="KL_DIVERGENCE", main=DBDs[k])
            axis(1, at=1:length(ListMotivIDs), labels=namen, las=2, cex.axis=0.8)
            dev.off()
        }
      }
      }
    }
  }
}
