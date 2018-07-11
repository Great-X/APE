title: org.linphone

# org.linphone

[Google Play Store](https://play.google.com/store/apps/details?id=org.linphone)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
// Build fingerprint: 'google/hammerhead/hammerhead:6.0.1/MOB30H/2751534:user/release-keys'
// Revision: '11'
// ABI: 'arm'
// pid: 29713, tid: 29713, name: org.linphone  >>> org.linphone <<<
// signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0x28
//     r0 00000001  r1 00000000  r2 00000000  r3 b6cf82d4
//     r4 00000000  r5 9e4c27e0  r6 00000000  r7 00000000
//     r8 bec7d97c  r9 00000000  sl bec7d9c4  fp bec7d9f0
//     ip b6cebd4c  sp bec7d8c0  lr 9ea8f769  pc b6cae25e  cpsr 600f0030
// 
// backtrace:
//     #00 pc 0003825e  /system/lib/libc.so (fseeko+25)
//     #01 pc 002ff765  /data/app/org.linphone-1/lib/arm/liblinphone.so
//     #02 pc 0034032b  /data/app/org.linphone-1/lib/arm/liblinphone.so
//     #03 pc 0033fc65  /data/app/org.linphone-1/lib/arm/liblinphone.so (belle_sip_body_handler_send_chunk+72)
//     #04 pc 003408e5  /data/app/org.linphone-1/lib/arm/liblinphone.so
//     #05 pc 0033fc65  /data/app/org.linphone-1/lib/arm/liblinphone.so (belle_sip_body_handler_send_chunk+72)
//     #06 pc 00343337  /data/app/org.linphone-1/lib/arm/liblinphone.so
//     #07 pc 00341e59  /data/app/org.linphone-1/lib/arm/liblinphone.so
//     #08 pc 0034279f  /data/app/org.linphone-1/lib/arm/liblinphone.so (belle_sip_channel_set_ready+146)
//     #09 pc 0035cb71  /data/app/org.linphone-1/lib/arm/liblinphone.so
//     #10 pc 0035c707  /data/app/org.linphone-1/lib/arm/liblinphone.so
//     #11 pc 0033af89  /data/app/org.linphone-1/lib/arm/liblinphone.so (belle_sip_main_loop_run+616)
//     #12 pc 0033b177  /data/app/org.linphone-1/lib/arm/liblinphone.so (belle_sip_main_loop_sleep+38)
//     #13 pc 002d1733  /data/app/org.linphone-1/lib/arm/liblinphone.so (sal_iterate+10)
//     #14 pc 002f9f7d  /data/app/org.linphone-1/lib/arm/liblinphone.so (linphone_core_iterate+572)
//     #15 pc 006126af  /data/app/org.linphone-1/oat/arm/base.odex (offset 0x3a6000)

```



