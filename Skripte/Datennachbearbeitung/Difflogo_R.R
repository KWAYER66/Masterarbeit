#!/usr/bin/env Rscript
args <- commandArgs(TRUE)
if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager", repos = "http://cran.us.r-project.org")

BiocManager::install("DiffLogo")
library(DiffLogo)

listNetze <- list.files("D:/Masterarbeit/Predictions", full.names=TRUE)
for (i in 1:length(listNetze)){
  if (grepl("Auswertung", listNetze[i]) == FALSE){
  # 1. Fall ALLE
  if(strsplit(listNetze[i],'_')[1][[1]][2]==176){
    listpwms1 <- list.files("D:/Masterarbeit/Daten/PWM_shifts_full_ueberarbeitet", pattern="*.pwm", full.names=TRUE)
    listpwms2 <- list.files(listNetze[i] , pattern="*.pwm", full.names=TRUE)
    for (j in 1:length(listpwms1))
    {
      pwm1 <- t(as.matrix(read.table(listpwms1[j], skip =1)))
      pwm2 <- t(as.matrix(read.table(listpwms2[j], skip =1)))
      ausgabename = paste(paste(listNetze[i],"/pdfs/",sep=""),paste(strsplit(listpwms1[j],"/")[1][[1]][5],".pdf",sep=""),sep="")
      pdf(file = ausgabename, width = 50, height = 25)
      diffLogoFromPwm(pwm1 = pwm1, pwm2 = pwm2)
      seqLogo(pwm1)
      seqLogo(pwm2)
      dev.off()
    }
  }else if(strsplit(listNetze[i],'_')[1][[1]][2]==140){
    #F�r Gruppen
    listpwms1 <- list.files("D:/Masterarbeit/Daten/PWMS_Nach_Gruppen_ueberarbeitet/AlleZusammen", pattern="*.pwm", full.names=TRUE)
    listpwms2 <- list.files(listNetze[i], pattern="*.pwm", full.names=TRUE)
    for (j in 1:length(listpwms1))
    {
      pwm1 <- t(as.matrix(read.table(listpwms1[j], skip =1)))
      pwm2 <- t(as.matrix(read.table(listpwms2[j], skip =1)))
      ausgabename = paste(paste(listNetze[i],"/pdfs/",sep=""),paste(strsplit(listpwms1[j],"/")[1][[1]][6],".pdf",sep=""),sep="")
      pdf(file = ausgabename, width = 50, height = 25)
      diffLogoFromPwm(pwm1 = pwm1, pwm2 = pwm2)
      seqLogo(pwm1)
      seqLogo(pwm2)
      dev.off()
    }
  }
  }
}
