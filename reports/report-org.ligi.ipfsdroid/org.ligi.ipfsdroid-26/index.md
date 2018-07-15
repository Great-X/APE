title: org.ligi.ipfsdroid

# org.ligi.ipfsdroid

[Google Play Store](https://play.google.com/store/apps/details?id=org.ligi.ipfsdroid)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.net.SocketTimeoutException: failed to connect to ipfs.io/173.252.100.21 (port 80) after 10000ms
// 	at libcore.io.IoBridge.connectErrno(IoBridge.java:169)
// 	at libcore.io.IoBridge.connect(IoBridge.java:122)
// 	at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:183)
// 	at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:452)
// 	at java.net.Socket.connect(Socket.java:884)
// 	at okhttp3.internal.platform.AndroidPlatform.connectSocket(AndroidPlatform.java:63)
// 	at okhttp3.internal.connection.RealConnection.connectSocket(RealConnection.java:223)
// 	at okhttp3.internal.connection.RealConnection.connect(RealConnection.java:149)
// 	at okhttp3.internal.connection.StreamAllocation.findConnection(StreamAllocation.java:195)
// 	at okhttp3.internal.connection.StreamAllocation.findHealthyConnection(StreamAllocation.java:121)
// 	at okhttp3.internal.connection.StreamAllocation.newStream(StreamAllocation.java:100)
// 	at okhttp3.internal.connection.ConnectInterceptor.intercept(ConnectInterceptor.java:42)
// 	at okhttp3.internal.http.RealInterceptorChain.proceed(RealInterceptorChain.java:92)
// 	at okhttp3.internal.http.RealInterceptorChain.proceed(RealInterceptorChain.java:67)
// 	at okhttp3.internal.cache.CacheInterceptor.intercept(CacheInterceptor.java:93)
// 	at okhttp3.internal.http.RealInterceptorChain.proceed(RealInterceptorChain.java:92)
// 	at okhttp3.internal.http.RealInterceptorChain.proceed(RealInterceptorChain.java:67)
// 	at okhttp3.internal.http.BridgeInterceptor.intercept(BridgeInterceptor.java:93)
// 	at okhttp3.internal.http.RealInterceptorChain.proceed(RealInterceptorChain.java:92)
// 	at okhttp3.internal.http.RetryAndFollowUpInterceptor.intercept(RetryAndFollowUpInterceptor.java:120)
// 	at okhttp3.internal.http.RealInterceptorChain.proceed(RealInterceptorChain.java:92)
// 	at okhttp3.internal.http.RealInterceptorChain.proceed(RealInterceptorChain.java:67)
// 	at okhttp3.RealCall.getResponseWithInterceptorChain(RealCall.java:185)
// 	at okhttp3.RealCall.execute(RealCall.java:69)
// 	at org.ligi.ipfsdroid.IPFSDaemon.downloadFile(IPFSDaemon.kt:72)
// 	at org.ligi.ipfsdroid.IPFSDaemon.access$downloadFile(IPFSDaemon.kt:14)
// 	at org.ligi.ipfsdroid.IPFSDaemon$download$1.run(IPFSDaemon.kt:35)
// 	at java.lang.Thread.run(Thread.java:818)

```



