title: com.jbirdvegas.mgerrit

# com.jbirdvegas.mgerrit

[Google Play Store](https://play.google.com/store/apps/details?id=com.jbirdvegas.mgerrit)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke interface method 'boolean java.util.Map.isEmpty()' on a null object reference
// 	at com.jbirdvegas.mgerrit.tasks.CommitProcessor.doInsert(CommitProcessor.java:123)
// 	at com.jbirdvegas.mgerrit.tasks.CommitProcessor.insert(CommitProcessor.java:56)
// 	at com.jbirdvegas.mgerrit.tasks.CommitProcessor.insert(CommitProcessor.java:43)
// 	at com.jbirdvegas.mgerrit.tasks.SyncProcessor$ResponseHandler.run(SyncProcessor.java:262)

```



