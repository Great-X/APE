title: io.github.hidroh.materialistic

# io.github.hidroh.materialistic

[Google Play Store](https://play.google.com/store/apps/details?id=io.github.hidroh.materialistic)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'int java.lang.String.length()' on a null object reference
// 	at io.github.hidroh.materialistic.widget.PeekabooTouchHelperCallback.drawPeekingText(PeekabooTouchHelperCallback.java:66)
// 	at io.github.hidroh.materialistic.widget.PeekabooTouchHelperCallback.onChildDraw(PeekabooTouchHelperCallback.java:57)
// 	at android.support.v7.widget.helper.ItemTouchHelper$Callback.onDraw(ItemTouchHelper.java:1957)
// 	at android.support.v7.widget.helper.ItemTouchHelper.onDraw(ItemTouchHelper.java:547)
// 	at android.support.v7.widget.RecyclerView.onDraw(RecyclerView.java:4078)
// 	at android.view.View.draw(View.java:16184)
// 	at android.support.v7.widget.RecyclerView.draw(RecyclerView.java:4013)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15180)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ViewGroup.recreateChildDisplayList(ViewGroup.java:3593)
// 	at android.view.ViewGroup.dispatchGetDisplayList(ViewGroup.java:3573)
// 	at android.view.View.updateDisplayListIfDirty(View.java:15140)
// 	at android.view.ThreadedRenderer.updateViewTreeDisplayList(ThreadedRenderer.java:281)
// 	at android.view.ThreadedRenderer.updateRootDisplayList(ThreadedRenderer.java:287)
// 	at android.view.ThreadedRenderer.draw(ThreadedRenderer.java:322)
// 	at android.view.ViewRootImpl.draw(ViewRootImpl.java:2615)
// 	at android.view.ViewRootImpl.performDraw(ViewRootImpl.java:2434)
// 	at android.view.ViewRootImpl.performTraversals(ViewRootImpl.java:2067)
// 	at android.view.ViewRootImpl.doTraversal(ViewRootImpl.java:1107)
// 	at android.view.ViewRootImpl$TraversalRunnable.run(ViewRootImpl.java:6013)
// 	at android.view.Choreographer$CallbackRecord.run(Choreographer.java:858)
// 	at android.view.Choreographer.doCallbacks(Choreographer.java:670)
// 	at android.view.Choreographer.doFrame(Choreographer.java:606)
// 	at android.view.Choreographer$FrameDisplayEventReceiver.run(Choreographer.java:844)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



