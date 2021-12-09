listNetze <- list.files("D:/Masterarbeit/Predictions", full.names=TRUE)


for (i in 1:length(listNetze)){
  if (grepl("Auswertung", listNetze[i]) == FALSE){
    data <- read.table(paste(listNetze[i], '/kl_divergencenGegenListePlot.tsv', sep=""))
    data2 <- read.table(paste(listNetze[i], '/kl_div_median_testdata.tsv', sep=""), header=FALSE)
    #ausgabename <- paste(listNetze[i], '/PLOT_kl_div_median_TESTDATEN.pdf', sep="")
    #pdf(file = ausgabename, width = 10, height = 10)
    ausgabename <- paste(listNetze[i], '/PLOT_kl_div_median_TESTDATEN.png', sep="")
    png(file = ausgabename, width=600, height=400)
    plot(data[1:dim(data)[1],], main = 'KL_Divergenz je geschätzte PWM (Testdaten) mit Median', ylab = 'KL_Divergenz', xlab='Index PWM', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
    abline(h=data2[1,1], col='blue')
    text(data2[1,1]+50,data2[1,1]+2, round(data2[1,1],4), col ="red", cex=2)
    dev.off()
    
    
    data <- read.table(paste(listNetze[i], '/kl_divergencen.tsv', sep=""))
    data2 <- read.table(paste(listNetze[i], '/mediankl_div.tsv', sep=""), header=FALSE)
    ausgabename <- paste(listNetze[i], '/PLOT_kl_div_median_ALLE.png', sep="")
    png(file = ausgabename, width=600, height=400)
    plot(data[1:dim(data)[1],], main = 'KL_Divergenz je geschätzte PWM mit Median', ylab = 'KL_Divergenz', xlab='Index PWM', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
    abline(h=data2[1,1], col='blue')
    text(data2[1,1]+100,data2[1,1]+3, round(data2[1,1],4), col ="red", cex=2)
    dev.off()
    
    data <- read.table(paste(listNetze[i], '/training.log', sep=""), header = TRUE)
    j = 100
    ausgabename <- paste(listNetze[i], '/PLOT_Loss_Epochen.png', sep="")
    png(file = ausgabename, width=600, height=400)
    plot(data$loss, main = 'Relation Loss zu Epochen', ylab = 'KL-Divergenz', xlab = 'Epochen', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
    while (j < length(data$loss)){
      abline(v= j, col = 'blue')
      text(j+120,2, round(data$loss[j],4), col = "blue", cex=2)
      if (j == 100){
        j = j + 400
      }else if (j > 100){
        j = j +500
      }
    }
    dev.off()
    
    
  }
}


for (i in 1:length(listNetze)){
  if (grepl("prediction029_176_1_1_4_500", listNetze[i]) == TRUE){
    data <- read.table(paste(listNetze[i], '/training.log', sep=""), header = TRUE)
    j = 100
    ausgabename <- paste(listNetze[i], '/PLOT_Loss_Epochen.png', sep="")
    png(file = ausgabename, width=600, height=400)
    plot(data$loss, main = 'Relation Loss zu Epochen', ylab = 'KL-Divergenz', xlab = 'Epochen', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
    while (j < length(data$loss)){
      abline(v= j, col = 'blue')
      text(j+120,200, round(data$loss[j],4), col = "blue", cex=2)
      if (j == 100){
        j = j + 400
      }else if (j > 100){
        j = j +500
      }
    }
    dev.off()
  }}


