


listNetze <- list.files("D:/Masterarbeit/Predictions", full.names=TRUE)
listNetze
data <- read.table(paste(listNetze[36], '/zuordgruppenplotdaten.tsv', sep=""))
data
for (k in 1:dim(data)[1]){
  if (data$V1[k] != data$V2[k]){
    data$V2[k] = NA
  }}


for (i in 1:length(listNetze)){
  if (grepl("Auswertung", listNetze[i]) == FALSE){
    list <- list.files(listNetze[i])
    for (j in 1:length(list)){
      if (grepl("zuordgruppenplotdaten", list[j]) == TRUE){
        
        data <- read.table(paste(listNetze[i], '/zuordgruppenplotdaten.tsv', sep=""))
        for (k in 1:dim(data)[1]){
          if (data$V1[k] != data$V2[k]){
            data$V2[k] = NA
          }}
        
        ausgabename <- paste(listNetze[i], '/Hist_Gruppierungen.pdf', sep="")
        
        p1 <- hist(data$V1, breaks=c(seq(0,50)), ylim = c(0,1400), xlim = c(0,50))
        p2 <- hist(data$V2, breaks=c(seq(0,50)), ylim = c(0,1400), xlim = c(0,50), add=T)
        pdf(file = ausgabename, width = 10, height = 10)
        plot(p1, col=rgb(0,0,1,1/4), xlim=c(0,50), ylim=c(0,1200), main = 'Korrekt vorhergesagte Zuordnungen', xlab='Gruppen 0 bis 50')
        plot(p2, col=rgb(1,0,0,1/4), xlim=c(0,50), add=T)
        legend("topright",legend=c("Tatsaechliche Zuordnung", "Geschaetzte Zuordnung"), lty=c(1,2), col = c(rgb(0,0,1,1/4), rgb(1,0,0,1/4)), bty= "n")
        dev.off()
      }
      if (grepl("zuordgruppenplottestdaten", list[j]) == TRUE){
        
        data <- read.table(paste(listNetze[i], '/zuordgruppenplottestdaten.tsv', sep=""))
        for (k in 1:dim(data)[1]){
          if (data$V1[k] != data$V2[k]){
            data$V2[k] = NA
          }}
        
        ausgabename <- paste(listNetze[i], '/Hist_Gruppierungen_Testdata.pdf', sep="")
        
        p1 <- hist(data$V1, breaks=c(seq(0,50)), ylim = c(0,400), xlim = c(0,50))
        p2 <- hist(data$V2, breaks=c(seq(0,50)), ylim = c(0,400), xlim = c(0,50))
        pdf(file = ausgabename, width = 10, height = 10)
        plot(p1, col=rgb(0,0,1,1/4), xlim=c(0,50), ylim=c(0,400), main = 'Korrekt vorhergesagte Zuordnungen', xlab='Gruppen 0 bis 50')
        plot(p2, col=rgb(1,0,0,1/4), xlim=c(0,50), add=T)
        legend("topright",legend=c("Tatsaechliche Zuordnung", "Geschaetzte Zuordnung"), lty=c(1,2), col = c(rgb(0,0,1,1/4), rgb(1,0,0,1/4)), bty= "n")
        dev.off()
      }
      
    }
  }
}


