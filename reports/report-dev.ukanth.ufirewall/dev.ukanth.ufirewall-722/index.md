title: dev.ukanth.ufirewall

# dev.ukanth.ufirewall

[Google Play Store](https://play.google.com/store/apps/details?id=dev.ukanth.ufirewall)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// android.view.ViewRootImpl$CalledFromWrongThreadException: Only the original thread that created a view hierarchy can touch its views.
// 	at android.view.ViewRootImpl.checkThread(ViewRootImpl.java:6556)
// 	at android.view.ViewRootImpl.requestLayout(ViewRootImpl.java:907)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.view.View.requestLayout(View.java:18728)
// 	at android.widget.AbsListView.requestLayout(AbsListView.java:1975)
// 	at android.widget.AdapterView$AdapterDataSetObserver.onChanged(AdapterView.java:840)
// 	at android.widget.AbsListView$AdapterDataSetObserver.onChanged(AbsListView.java:6203)
// 	at android.database.DataSetObservable.notifyChanged(DataSetObservable.java:37)
// 	at android.widget.BaseAdapter.notifyDataSetChanged(BaseAdapter.java:50)
// 	at android.preference.PreferenceGroupAdapter.onPreferenceChange(PreferenceGroupAdapter.java:271)
// 	at android.preference.Preference.notifyChanged(Preference.java:1147)
// 	at android.preference.TwoStatePreference.setChecked(TwoStatePreference.java:84)
// 	at dev.ukanth.ufirewall.preferences.ExpPreferenceFragment.updateLeakCheckbox(ExpPreferenceFragment.java:195)
// 	at dev.ukanth.ufirewall.preferences.ExpPreferenceFragment.lambda$updateFixLeakScript$1$ExpPreferenceFragment(ExpPreferenceFragment.java:181)
// 	at dev.ukanth.ufirewall.preferences.ExpPreferenceFragment$$Lambda$1.run(Unknown Source)
// 	at java.lang.Thread.run(Thread.java:818)

```



