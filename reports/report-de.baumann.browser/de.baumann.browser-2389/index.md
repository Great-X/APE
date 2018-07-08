title: de.baumann.browser

# de.baumann.browser

[Google Play Store](https://play.google.com/store/apps/details?id=de.baumann.browser)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IndexOutOfBoundsException: Invalid index 0, size is 0
// 	at java.util.ArrayList.throwIndexOutOfBoundsException(ArrayList.java:255)
// 	at java.util.ArrayList.get(ArrayList.java:308)
// 	at de.baumann.browser.View.CompleteAdapter.getView(CompleteAdapter.java:181)
// 	at android.widget.AbsListView.obtainView(AbsListView.java:2346)
// 	at android.widget.ListPopupWindow$DropDownListView.obtainView(ListPopupWindow.java:1734)
// 	at android.widget.ListView.measureHeightOfChildren(ListView.java:1281)
// 	at android.widget.ListPopupWindow.buildDropDown(ListPopupWindow.java:1209)
// 	at android.widget.ListPopupWindow.show(ListPopupWindow.java:584)
// 	at android.widget.AutoCompleteTextView.showDropDown(AutoCompleteTextView.java:1106)
// 	at android.widget.AutoCompleteTextView.updateDropDownForFilter(AutoCompleteTextView.java:975)
// 	at android.widget.AutoCompleteTextView.onFilterComplete(AutoCompleteTextView.java:957)
// 	at android.widget.Filter$ResultsHandler.handleMessage(Filter.java:285)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



