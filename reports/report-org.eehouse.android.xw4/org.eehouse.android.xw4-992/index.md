title: org.eehouse.android.xw4

# org.eehouse.android.xw4

[Google Play Store](https://play.google.com/store/apps/details?id=org.eehouse.android.xw4)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
// Build fingerprint: 'google/hammerhead/hammerhead:6.0.1/MOB30H/2751534:user/release-keys'
// Revision: '11'
// ABI: 'arm'
// pid: 21202, tid: 21264, name: Thread-1042  >>> org.eehouse.android.xw4 <<<
// signal 6 (SIGABRT), code -6 (SI_TKILL), fault addr --------
// Abort message: 'art/runtime/thread.cc:1336] No pending exception expected: java.lang.NullPointerException: Attempt to invoke virtual method 'boolean org.eehouse.android.xw4.jni.JNIThread.busy()' on a null object reference'
//     r0 00000000  r1 00005310  r2 00000006  r3 9cb3d978
//     r4 9cb3d980  r5 9cb3d930  r6 00000001  r7 0000010c
//     r8 b4c3f7f0  r9 b4c3de38  sl 9e9ffda0  fp b4c247ec
//     ip 00000006  sp 9cb3cf98  lr b6c8fb61  pc b6c91f50  cpsr 40070010
// 
// backtrace:
//     #00 pc 00041f50  /system/lib/libc.so (tgkill+12)
//     #01 pc 0003fb5d  /system/lib/libc.so (pthread_kill+32)
//     #02 pc 0001c30f  /system/lib/libc.so (raise+10)
//     #03 pc 000194c1  /system/lib/libc.so (__libc_android_abort+34)
//     #04 pc 000174ac  /system/lib/libc.so (abort+4)
//     #05 pc 0032848d  /system/lib/libart.so (_ZN3art7Runtime5AbortEv+212)
//     #06 pc 000fd6fd  /system/lib/libart.so (_ZN3art10LogMessageD2Ev+1284)
//     #07 pc 000fa76f  /system/lib/libart.so (_ZN3art7BarrierD2Ev+182)
//     #08 pc 0034e819  /system/lib/libart.so (_ZN3art10ThreadList4DumpERNSt3__113basic_ostreamIcNS1_11char_traitsIcEEEE+144)
//     #09 pc 0032854d  /system/lib/libart.so (_ZN3art7Runtime5AbortEv+404)
//     #10 pc 000fd6fd  /system/lib/libart.so (_ZN3art10LogMessageD2Ev+1284)
//     #11 pc 00342ead  /system/lib/libart.so (_ZNK3art6Thread24AssertNoPendingExceptionEv.part.170+360)
//     #12 pc 0013ad53  /system/lib/libart.so (_ZN3art11ClassLinker9FindClassEPNS_6ThreadEPKcNS_6HandleINS_6mirror11ClassLoaderEEE+26)
//     #13 pc 0029cc6d  /system/lib/libart.so (_ZN3art3JNI9FindClassEP7_JNIEnvPKc+772)
//     #14 pc 000120cf  /data/app/org.eehouse.android.xw4-1/lib/arm/libxwjni.so (getCurSeconds+22)
//     #15 pc 0000d78f  /data/app/org.eehouse.android.xw4-1/lib/arm/libxwjni.so (and_util_getCurSeconds+14)
//     #16 pc 0001e6bf  /data/app/org.eehouse.android.xw4-1/lib/arm/libxwjni.so (server_do+1682)
//     #17 pc 0000be01  /data/app/org.eehouse.android.xw4-1/lib/arm/libxwjni.so (Java_org_eehouse_android_xw4_jni_XwJNI_server_1do+64)
//     #18 pc 00425c31  /data/app/org.eehouse.android.xw4-1/oat/arm/base.odex (offset 0x321000)

```



