title: de.retujo.bierverkostung

# de.retujo.bierverkostung

[Google Play Store](https://play.google.com/store/apps/details?id=de.retujo.bierverkostung)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: An error occurred while executing doInBackground()
// 	at android.os.AsyncTask$3.done(AsyncTask.java:309)
// 	at java.util.concurrent.FutureTask.finishCompletion(FutureTask.java:354)
// 	at java.util.concurrent.FutureTask.setException(FutureTask.java:223)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:242)
// 	at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:234)
// 	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1113)
// 	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:588)
// 	at java.lang.Thread.run(Thread.java:818)
// Caused by: de.retujo.bierverkostung.exchange.ExportImportException: Failed to close ZipFileWriter!
// 	at de.retujo.bierverkostung.beer.BeerExporter.tryToClose(BeerExporter.java:168)
// 	at de.retujo.bierverkostung.beer.BeerExporter.exportAllBeers(BeerExporter.java:197)
// 	at de.retujo.bierverkostung.beer.BeerExporter.exportAllBeers(BeerExporter.java:175)
// 	at de.retujo.bierverkostung.beer.BeerExporter.doInBackground(BeerExporter.java:100)
// 	at de.retujo.bierverkostung.beer.BeerExporter.doInBackground(BeerExporter.java:51)
// 	at android.os.AsyncTask$2.call(AsyncTask.java:295)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
// 	... 4 more
// Caused by: java.util.zip.ZipException: No entries
// 	at java.util.zip.ZipOutputStream.finish(ZipOutputStream.java:301)
// 	at java.util.zip.ZipOutputStream.close(ZipOutputStream.java:152)
// 	at de.retujo.bierverkostung.exchange.ZipFileWriter.close(ZipFileWriter.java:185)
// 	at de.retujo.bierverkostung.beer.BeerExporter.tryToClose(BeerExporter.java:166)
// 	... 10 more

```



