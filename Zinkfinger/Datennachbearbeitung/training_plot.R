listNetze <- list.files("/ZinkFinger/Predictions", full.names=TRUE)


for (i in 1:length(listNetze)){
  if (grepl("prediction", listNetze[i]) == TRUE){
    
    data <- read.table(paste(listNetze[i], '/training.log', sep=""), header = TRUE)
    j = 100
    ausgabename <- paste(listNetze[i], '/PLOT_Loss_Epochen.pdf', sep="")
    pdf(file = ausgabename, width = 15, height = 15)
    plot(data$loss, main = 'Relation Loss zu Epochen', ylab = 'KL-Divergence Loss', xlab = 'Epochen')
    while (j < length(data$loss)){
      abline(v= j, col = 'blue')
      text(j+120,2, round(data$loss[j],4), col = "blue")
      if (j == 100){
        j = j + 400
      }else if (j > 100){
        j = j +500
      }
    }
    dev.off()
    
    
  }
}
