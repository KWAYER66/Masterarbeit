listNetze <- list.files("D:/Masterarbeit/Predictions", full.names=TRUE)


for (i in 1:length(listNetze)){
  if (grepl("Auswertung", listNetze[i]) == FALSE){
    list <- list.files(listNetze[i])
    for (j in 1:length(list)){
      if (grepl("Sicherheitsmass_alle", list[j]) == TRUE){
        
        data <- read.table(paste(listNetze[i], '/kl_divergencen.tsv', sep=""))
        data2 <- as.matrix(read.table(paste(listNetze[i], '/Sicherheitsmass_alle.tsv', sep=""), header=FALSE))
        print('hi')
        ausgabename <- paste(listNetze[i], '/Scatterplot_Sicherheitsmas_KL_Div.png', sep="")
        png(file = ausgabename, width=600, height=400)
        plot(data2[,1], data[,1], main = 'Scatterplot: Sicherheitsmass gegen KL-Div', ylab = 'KL_Div', xlab = 'Sicherheitsmass', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
        dev.off()
      }
    }
  }
}
