title: fr.free.nrw.commons

# fr.free.nrw.commons

[Google Play Store](https://play.google.com/store/apps/details?id=fr.free.nrw.commons)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
// Build fingerprint: 'google/hammerhead/hammerhead:6.0.1/MOB30H/2751534:user/release-keys'
// Revision: '11'
// ABI: 'arm'
// pid: 12841, tid: 12841, name: ree.nrw.commons  >>> fr.free.nrw.commons <<<
// signal 6 (SIGABRT), code -6 (SI_TKILL), fault addr --------
// Abort message: '[FATAL:jni_android.cc(249)] Check failed: false. Please include Java exception stack in crash report
// '
//     r0 00000000  r1 00003229  r2 00000006  r3 b6f13b7c
//     r4 b6f13b84  r5 b6f13b34  r6 0000000b  r7 0000010c
//     r8 b6cbcec0  r9 be8d0b80  sl 00000000  fp 0020001d
//     ip 00000006  sp be8d0698  lr b6c82b61  pc b6c84f50  cpsr 400f0010
// 
// backtrace:
//     #00 pc 00041f50  /system/lib/libc.so (tgkill+12)
//     #01 pc 0003fb5d  /system/lib/libc.so (pthread_kill+32)
//     #02 pc 0001c30f  /system/lib/libc.so (raise+10)
//     #03 pc 000194c1  /system/lib/libc.so (__libc_android_abort+34)
//     #04 pc 000174ac  /system/lib/libc.so (abort+4)
//     #05 pc 002b9125  /system/app/WebViewGoogle/WebViewGoogle.apk (offset 0x7f2000)

```



