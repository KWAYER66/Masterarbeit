#!/usr/bin/env Rscript
args <- commandArgs(TRUE)
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager", repos = "http://cran.us.r-project.org")

BiocManager::install("DiffLogo")
library(DiffLogo)
pwm1
seqLogo(pwm1)

listNetze <- list.files("D:/Masterarbeit/Predictions", full.names=TRUE)
for (i in 1:length(listNetze)){
  if (grepl("prediction", listNetze[i]) == TRUE){
  # 1. Fall ALLE
  if(strsplit(listNetze[i],'_')[1][[1]][2]==176){
    listpwms1 <- list.files("D:/Masterarbeit/Daten/PWM_shifts_full_ueberarbeitet", pattern="*.pwm", full.names=TRUE)
    listpwms2 <- list.files(listNetze[i] , pattern="*.pwm", full.names=TRUE)
    for (j in 1:length(listpwms1))
    {
      pwm1 <- t(as.matrix(read.table(listpwms1[j], skip =1)))
      pwm2 <- t(as.matrix(read.table(listpwms2[j], skip =1)))
      ausgabename = paste(paste(listNetze[i],"/pdfs/",sep=""),paste(strsplit(listpwms1[j],"/")[1][[1]][5],".pdf",sep=""),sep="")
      pdf(file = ausgabename, width = 12, height = 6)
      diffLogoFromPwm(pwm1 = pwm1, pwm2 = pwm2)
      seqLogo(pwm1, main = 'pwm')
      seqLogo(pwm2, main = 'Vorhersage')
      dev.off()
    }
  }
  }
}
