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
// Caused by: java.lang.IllegalArgumentException: Failed to create a FileOutputStream for </storage/emulated/Beers_2018-07-08T043127.zip>!
// 	at de.retujo.bierverkostung.exchange.ZipFileWriter.tryToCreateFileOutputStream(ZipFileWriter.java:75)
// 	at de.retujo.bierverkostung.exchange.ZipFileWriter.getInstance(ZipFileWriter.java:67)
// 	at de.retujo.bierverkostung.beer.BeerExporter.exportAllBeers(BeerExporter.java:186)
// 	at de.retujo.bierverkostung.beer.BeerExporter.exportAllBeers(BeerExporter.java:175)
// 	at de.retujo.bierverkostung.beer.BeerExporter.doInBackground(BeerExporter.java:100)
// 	at de.retujo.bierverkostung.beer.BeerExporter.doInBackground(BeerExporter.java:51)
// 	at android.os.AsyncTask$2.call(AsyncTask.java:295)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
// 	... 4 more
// Caused by: java.io.FileNotFoundException: /storage/emulated/Beers_2018-07-08T043127.zip: open failed: EACCES (Permission denied)
// 	at libcore.io.IoBridge.open(IoBridge.java:452)
// 	at java.io.FileOutputStream.<init>(FileOutputStream.java:87)
// 	at java.io.FileOutputStream.<init>(FileOutputStream.java:72)
// 	at de.retujo.bierverkostung.exchange.ZipFileWriter.tryToCreateFileOutputStream(ZipFileWriter.java:72)
// 	... 11 more
// Caused by: android.system.ErrnoException: open failed: EACCES (Permission denied)
// 	at libcore.io.Posix.open(Native Method)
// 	at libcore.io.BlockGuardOs.open(BlockGuardOs.java:186)
// 	at libcore.io.IoBridge.open(IoBridge.java:438)
// 	... 14 more

```



