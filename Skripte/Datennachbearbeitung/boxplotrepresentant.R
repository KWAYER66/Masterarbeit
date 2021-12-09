listNetze <- list.files("D:/Masterarbeit/Predictions", full.names=TRUE)




for (i in 1:length(listNetze)){
  if (grepl("Auswertung", listNetze[i]) == FALSE){
    #1. Fall ALLE Representant und Andere
    data <- read.table(paste(listNetze[i], '/kl_divergencenrepresentanten.tsv', sep=""))
    data2 <- read.table(paste(listNetze[i], '/kl_divergencenandere.tsv', sep=""), header=FALSE)
    
    ausgabename <- paste(listNetze[i], '/Boxplot_Representanten_ALLE.png', sep="")
    png(file = ausgabename, width=600, height=400)
    boxplot(data$V2,data2$V2, main = 'Boxplot: Representanten und Andere (ALLE)', ylab ='KL-Divergence', names =c("Representant", "Andere"), cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
    dev.off()
    
    #2. Fall TESTDATA Representant und Andere
    data <- read.table(paste(listNetze[i], '/kl_divergencenrepresentantentestdata.tsv', sep=""))
    data2 <- read.table(paste(listNetze[i], '/kl_divergencenanderetestdata.tsv', sep=""), header=FALSE)
    
    ausgabename <- paste(listNetze[i], '/Boxplot_Representanten_Testdata.png', sep="")
    png(file = ausgabename, width=600, height=400)
    boxplot(data$V2,data2$V2, main = 'Boxplot: Representanten und Andere (Testdaten)', ylab ='KL-Divergence', names =c("Representant", "Andere"), cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
    dev.off()   
    #3. Fall TESTDATA Representant und Andere
    data <- read.table(paste(listNetze[i], '/kl_divergencenrepresentantentraindata.tsv', sep=""))
    data2 <- read.table(paste(listNetze[i], '/kl_divergencenanderetraindata.tsv', sep=""), header=FALSE)
    
    ausgabename <- paste(listNetze[i], '/Boxplot_Representanten_Traindata.png', sep="")
    png(file = ausgabename, width=600, height=400)
    boxplot(data$V2,data2$V2, main = 'Boxplot: Representanten und Andere (Trainingsdaten)', ylab ='KL-Divergence', names =c("Representant", "Andere"), cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
    dev.off()   
    
  }
}
