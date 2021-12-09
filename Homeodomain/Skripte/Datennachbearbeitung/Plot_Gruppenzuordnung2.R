


listNetze <- list.files("D:/Masterarbeit/Predictions", full.names=TRUE)


test <- read.table('D:/Masterarbeit/Predictions/prediction014_176_1_1_4_500/zuordgruppenplotdaten.tsv')
test <- test +1
a <-hist(test$V1, breaks=seq(from=0, to=51, by=1))
b <-hist(test$V2, breaks=seq(from=0, to=51, by=1))
plot(a, col=rgb(0,0,1,1/4), xlim=c(0,51), ylim=c(0,1200), main = 'Korrekt vorhergesagte Zuordnungen', xlab='Gruppen 0 bis 50', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
plot(b, col=rgb(1,0,0,1/4), xlim=c(0,51), add=T)
legend(0, 1000,legend=c("Tatsaechliche Zuordnung", "Geschaetzte Zuordnung"), lty=1:2, col = c(rgb(0,0,1,1/4), rgb(1,0,0,1/4)), bty= "n")
legend(100, 1000, legend=c("Line 1", "Line 2"),
       col=c("red", "blue"), lty=1:2, cex=0.8)
hist(table(test$V1), breaks=100)
legend(100, 1000, legend=c("Line 1", "Line 2"),
       col=c("red", "blue"), lty=1:2, cex=0.8)
table(test$V1+1)[1][[0:50]]
tt <-1:51
for (i in 1:51){
  tt[i] <- table(test$V1)[i][[1]]
}
tt
hist(y)
table(test$V1)[1][[2]]

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
        
        ausgabename <- paste(listNetze[i], '/Hist_Gruppierungen.png', sep="")
        
        p1 <- hist(data$V1, breaks=seq(from=0, to=51, by=1), ylim = c(0,1400), xlim = c(0,51))
        p2 <- hist(data$V2, breaks=seq(from=0, to=51, by=1), ylim = c(0,1400), xlim = c(0,51), add=T)
        png(file = ausgabename, width=600, height=400)
        plot(p1, col=rgb(0,0,1,1/4), xlim=c(0,51), ylim=c(0,1200), main = 'Korrekt vorhergesagte Zuordnungen', xlab='Gruppen 0 bis 50', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
        plot(p2, col=rgb(1,0,0,1/4), xlim=c(0,51), add=T)
        legend("topright",legend=c("Tatsaechliche Zuordnung", "Geschaetzte Zuordnung"), lty=c(1,2), col = c(rgb(0,0,1,1/4), rgb(1,0,0,1/4)), bty= "n", cex=1.5)
        dev.off()
      }
      if (grepl("zuordgruppenplottestdaten", list[j]) == TRUE){
        
        data <- read.table(paste(listNetze[i], '/zuordgruppenplottestdaten.tsv', sep=""))
        for (k in 1:dim(data)[1]){
          if (data$V1[k] != data$V2[k]){
            data$V2[k] = NA
          }}
        
        ausgabename <- paste(listNetze[i], '/Hist_Gruppierungen_Testdata.png', sep="")
        
        p1 <- hist(data$V1, breaks=c(seq(0,50)), ylim = c(0,400), xlim = c(0,50))
        p2 <- hist(data$V2, breaks=c(seq(0,50)), ylim = c(0,400), xlim = c(0,50))
        png(file = ausgabename, width=600, height=400)
        plot(p1, col=rgb(0,0,1,1/4), xlim=c(0,50), ylim=c(0,400), main = 'Korrekt vorhergesagte Zuordnungen', xlab='Gruppen 0 bis 50', cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
        plot(p2, col=rgb(1,0,0,1/4), xlim=c(0,50), add=T)
        legend("topright",legend=c("Tatsaechliche Zuordnung", "Geschaetzte Zuordnung"), lty=c(1,2), col = c(rgb(0,0,1,1/4), rgb(1,0,0,1/4)), bty= "n")
        dev.off()
      }
      
    }
  }
}


