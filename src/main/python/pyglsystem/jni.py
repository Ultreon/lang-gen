from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.nio.IntBuffer as IntBuffer
import java.lang.reflect.Field as Field
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.reflect.Field as _Field
_Field = _Field
import java.nio.DoubleBuffer as _DoubleBuffer
_DoubleBuffer = _DoubleBuffer
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.reflect.Method as _Method
_Method = _Method
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import org.lwjgl.system.jni.JNINativeInterface as _JNINativeInterface
_JNINativeInterface = _JNINativeInterface
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.reflect.Method as Method
import java.lang.Class as _Class
_Class = _Class
 
class JNINativeInterface():
    """org.lwjgl.system.jni.JNINativeInterface"""
 
    @staticmethod
    def _wrap(java_value: _JNINativeInterface) -> 'JNINativeInterface':
        return JNINativeInterface(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JNINativeInterface):
        """
        Dynamic initializer for JNINativeInterface.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JNINativeInterface__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JNINativeInterface__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nSetByteArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetByteArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nSetByteArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetFloatArrayElements(arg0: 'float', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetFloatArrayElements(float[],long)"""
        return int._wrap(_JNINativeInterface.nGetFloatArrayElements(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def GetVersion() -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.GetVersion()"""
        return int._wrap(_JNINativeInterface.GetVersion())

    @staticmethod
    @overload
    def nReleaseCharArrayElements(arg0: 'char', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseCharArrayElements(char[],long,int)"""
        _JNINativeInterface.nReleaseCharArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nReleaseIntArrayElements(arg0: 'int', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseIntArrayElements(int[],long,int)"""
        _JNINativeInterface.nReleaseIntArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetBooleanArrayElements(arg0: bytes, arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetBooleanArrayElements(byte[],long)"""
        return int._wrap(_JNINativeInterface.nGetBooleanArrayElements(bytes, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetIntArrayElements(arg0: 'int', arg1: 'ByteBuffer') -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.jni.JNINativeInterface.GetIntArrayElements(int[],java.nio.ByteBuffer)"""
        return IntBuffer._wrap(_JNINativeInterface.GetIntArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def ToReflectedField(arg0: 'Class', arg1: int, arg2: bool) -> 'Field':
        """public static java.lang.reflect.Field org.lwjgl.system.jni.JNINativeInterface.ToReflectedField(java.lang.Class<?>,long,boolean)"""
        return Field._wrap(_JNINativeInterface.ToReflectedField(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def NewDirectByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.NewDirectByteBuffer(long,long)"""
        return ByteBuffer._wrap(_JNINativeInterface.NewDirectByteBuffer(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetIntArrayRegion(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetIntArrayRegion(int[],int,int,long)"""
        _JNINativeInterface.nGetIntArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

        @staticmethod
        @overload
        def noop():
            """public static native void org.lwjgl.system.jni.JNINativeInterface.noop()"""
            _JNINativeInterface.noop()

    @staticmethod
    @overload
    def nGetCharArrayRegion(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetCharArrayRegion(char[],int,int,long)"""
        _JNINativeInterface.nGetCharArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetLongArrayElements(arg0: 'long', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetLongArrayElements(long[],long)"""
        return int._wrap(_JNINativeInterface.nGetLongArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nSetShortArrayRegion(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetShortArrayRegion(short[],int,int,long)"""
        _JNINativeInterface.nSetShortArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetCharArrayElements(arg0: 'char', arg1: 'ByteBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.jni.JNINativeInterface.GetCharArrayElements(char[],java.nio.ByteBuffer)"""
        return ShortBuffer._wrap(_JNINativeInterface.GetCharArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nReleaseDoubleArrayElements(arg0: 'double', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseDoubleArrayElements(double[],long,int)"""
        _JNINativeInterface.nReleaseDoubleArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetByteArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetByteArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetByteArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def GetObjectRefType(arg0: object) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.GetObjectRefType(java.lang.Object)"""
        return int._wrap(_JNINativeInterface.GetObjectRefType(arg0))

    @staticmethod
    @overload
    def ReleaseFloatArrayElements(arg0: 'float', arg1: 'FloatBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseFloatArrayElements(float[],java.nio.FloatBuffer,int)"""
        _JNINativeInterface.ReleaseFloatArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetStringRegion(arg0: str, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetStringRegion(java.lang.String,int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetStringRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseDoubleArrayElements(arg0: 'double', arg1: 'DoubleBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseDoubleArrayElements(double[],java.nio.DoubleBuffer,int)"""
        _JNINativeInterface.ReleaseDoubleArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetShortArrayRegion(arg0: 'short', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetShortArrayRegion(short[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.GetShortArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetLongArrayRegion(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetLongArrayRegion(long[],int,int,long)"""
        _JNINativeInterface.nGetLongArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetStringUTFRegion(arg0: str, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetStringUTFRegion(java.lang.String,int,int,long)"""
        _JNINativeInterface.nGetStringUTFRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def NewWeakGlobalRef(arg0: object) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.NewWeakGlobalRef(java.lang.Object)"""
        return int._wrap(_JNINativeInterface.NewWeakGlobalRef(arg0))

    @staticmethod
    @overload
    def ReleaseCharArrayElements(arg0: 'char', arg1: 'ShortBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseCharArrayElements(char[],java.nio.ShortBuffer,int)"""
        _JNINativeInterface.ReleaseCharArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def ReleaseByteArrayElements(arg0: bytes, arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseByteArrayElements(byte[],java.nio.ByteBuffer,int)"""
        _JNINativeInterface.ReleaseByteArrayElements(bytes, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetJavaVM(arg0: int) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.nGetJavaVM(long)"""
        return int._wrap(_JNINativeInterface.nGetJavaVM(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nSetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetBooleanArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nSetBooleanArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nSetLongArrayRegion(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetLongArrayRegion(long[],int,int,long)"""
        _JNINativeInterface.nSetLongArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nToReflectedField(arg0: 'Class', arg1: int, arg2: bool) -> 'Field':
        """public static native java.lang.reflect.Field org.lwjgl.system.jni.JNINativeInterface.nToReflectedField(java.lang.Class<?>,long,boolean)"""
        return Field._wrap(_JNINativeInterface.nToReflectedField(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def GetFloatArrayRegion(arg0: 'float', arg1: int, arg2: 'FloatBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetFloatArrayRegion(float[],int,java.nio.FloatBuffer)"""
        _JNINativeInterface.GetFloatArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nNewDirectByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static native java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.nNewDirectByteBuffer(long,long)"""
        return ByteBuffer._wrap(_JNINativeInterface.nNewDirectByteBuffer(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nReleaseBooleanArrayElements(arg0: bytes, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseBooleanArrayElements(byte[],long,int)"""
        _JNINativeInterface.nReleaseBooleanArrayElements(bytes, _long.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nGetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetBooleanArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nGetBooleanArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def SetCharArrayRegion(arg0: 'char', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetCharArrayRegion(char[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.SetCharArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nReleaseShortArrayElements(arg0: 'short', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseShortArrayElements(short[],long,int)"""
        _JNINativeInterface.nReleaseShortArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def SetShortArrayRegion(arg0: 'short', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetShortArrayRegion(short[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.SetShortArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def SetByteArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetByteArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.SetByteArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def DeleteGlobalRef(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.DeleteGlobalRef(long)"""
        _JNINativeInterface.DeleteGlobalRef(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nGetIntArrayElements(arg0: 'int', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetIntArrayElements(int[],long)"""
        return int._wrap(_JNINativeInterface.nGetIntArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def SetLongArrayRegion(arg0: 'long', arg1: int, arg2: 'LongBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetLongArrayRegion(long[],int,java.nio.LongBuffer)"""
        _JNINativeInterface.SetLongArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def UnregisterNatives(arg0: 'Class') -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.UnregisterNatives(java.lang.Class<?>)"""
        return int._wrap(_JNINativeInterface.UnregisterNatives(arg0))

    @staticmethod
    @overload
    def GetDirectBufferAddress(arg0: 'Buffer') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.GetDirectBufferAddress(java.nio.Buffer)"""
        return int._wrap(_JNINativeInterface.GetDirectBufferAddress(arg0))

    @staticmethod
    @overload
    def nSetCharArrayRegion(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetCharArrayRegion(char[],int,int,long)"""
        _JNINativeInterface.nSetCharArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def ReleaseShortArrayElements(arg0: 'short', arg1: 'ShortBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseShortArrayElements(short[],java.nio.ShortBuffer,int)"""
        _JNINativeInterface.ReleaseShortArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def SetIntArrayRegion(arg0: 'int', arg1: int, arg2: 'IntBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetIntArrayRegion(int[],int,java.nio.IntBuffer)"""
        _JNINativeInterface.SetIntArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetStringRegion(arg0: str, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetStringRegion(java.lang.String,int,int,long)"""
        _JNINativeInterface.nGetStringRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nRegisterNatives(arg0: 'Class', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.nRegisterNatives(java.lang.Class<?>,long,int)"""
        return int._wrap(_JNINativeInterface.nRegisterNatives(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nReleaseByteArrayElements(arg0: bytes, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseByteArrayElements(byte[],long,int)"""
        _JNINativeInterface.nReleaseByteArrayElements(bytes, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nSetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetDoubleArrayRegion(double[],int,int,long)"""
        _JNINativeInterface.nSetDoubleArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetLongArrayElements(arg0: 'long', arg1: 'ByteBuffer') -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.jni.JNINativeInterface.GetLongArrayElements(long[],java.nio.ByteBuffer)"""
        return LongBuffer._wrap(_JNINativeInterface.GetLongArrayElements(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def GetJavaVM(arg0: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.jni.JNINativeInterface.GetJavaVM(org.lwjgl.PointerBuffer)"""
        return int._wrap(_JNINativeInterface.GetJavaVM(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nGetByteArrayElements(arg0: bytes, arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetByteArrayElements(byte[],long)"""
        return int._wrap(_JNINativeInterface.nGetByteArrayElements(bytes, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def SetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetBooleanArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.SetBooleanArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def FromReflectedField(arg0: 'Field') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.FromReflectedField(java.lang.reflect.Field)"""
        return int._wrap(_JNINativeInterface.FromReflectedField(arg0))

    @staticmethod
    @overload
    def nGetFloatArrayRegion(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetFloatArrayRegion(float[],int,int,long)"""
        _JNINativeInterface.nGetFloatArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def NewGlobalRef(arg0: object) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.NewGlobalRef(java.lang.Object)"""
        return int._wrap(_JNINativeInterface.NewGlobalRef(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def GetCharArrayRegion(arg0: 'char', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetCharArrayRegion(char[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.GetCharArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nReleaseFloatArrayElements(arg0: 'float', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseFloatArrayElements(float[],long,int)"""
        _JNINativeInterface.nReleaseFloatArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nSetFloatArrayRegion(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetFloatArrayRegion(float[],int,int,long)"""
        _JNINativeInterface.nSetFloatArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetCharArrayElements(arg0: 'char', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetCharArrayElements(char[],long)"""
        return int._wrap(_JNINativeInterface.nGetCharArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def ToReflectedMethod(arg0: 'Class', arg1: int, arg2: bool) -> 'Method':
        """public static java.lang.reflect.Method org.lwjgl.system.jni.JNINativeInterface.ToReflectedMethod(java.lang.Class<?>,long,boolean)"""
        return Method._wrap(_JNINativeInterface.ToReflectedMethod(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def GetFloatArrayElements(arg0: 'float', arg1: 'ByteBuffer') -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.jni.JNINativeInterface.GetFloatArrayElements(float[],java.nio.ByteBuffer)"""
        return FloatBuffer._wrap(_JNINativeInterface.GetFloatArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def GetLongArrayRegion(arg0: 'long', arg1: int, arg2: 'LongBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetLongArrayRegion(long[],int,java.nio.LongBuffer)"""
        _JNINativeInterface.GetLongArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseLongArrayElements(arg0: 'long', arg1: 'LongBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseLongArrayElements(long[],java.nio.LongBuffer,int)"""
        _JNINativeInterface.ReleaseLongArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetByteArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetByteArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nGetByteArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetBooleanArrayElements(arg0: bytes, arg1: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.GetBooleanArrayElements(byte[],java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_JNINativeInterface.GetBooleanArrayElements(bytes, arg1))

    @staticmethod
    @overload
    def GetDoubleArrayElements(arg0: 'double', arg1: 'ByteBuffer') -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.jni.JNINativeInterface.GetDoubleArrayElements(double[],java.nio.ByteBuffer)"""
        return DoubleBuffer._wrap(_JNINativeInterface.GetDoubleArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def GetShortArrayElements(arg0: 'short', arg1: 'ByteBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.jni.JNINativeInterface.GetShortArrayElements(short[],java.nio.ByteBuffer)"""
        return ShortBuffer._wrap(_JNINativeInterface.GetShortArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def DeleteWeakGlobalRef(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.DeleteWeakGlobalRef(long)"""
        _JNINativeInterface.DeleteWeakGlobalRef(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nDeleteWeakGlobalRef(arg0: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nDeleteWeakGlobalRef(long)"""
        _JNINativeInterface.nDeleteWeakGlobalRef(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ReleaseIntArrayElements(arg0: 'int', arg1: 'IntBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseIntArrayElements(int[],java.nio.IntBuffer,int)"""
        _JNINativeInterface.ReleaseIntArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetDoubleArrayRegion(double[],int,int,long)"""
        _JNINativeInterface.nGetDoubleArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def SetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetDoubleArrayRegion(double[],int,java.nio.DoubleBuffer)"""
        _JNINativeInterface.SetDoubleArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetShortArrayElements(arg0: 'short', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetShortArrayElements(short[],long)"""
        return int._wrap(_JNINativeInterface.nGetShortArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nToReflectedMethod(arg0: 'Class', arg1: int, arg2: bool) -> 'Method':
        """public static native java.lang.reflect.Method org.lwjgl.system.jni.JNINativeInterface.nToReflectedMethod(java.lang.Class<?>,long,boolean)"""
        return Method._wrap(_JNINativeInterface.nToReflectedMethod(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def nGetShortArrayRegion(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetShortArrayRegion(short[],int,int,long)"""
        _JNINativeInterface.nGetShortArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetBooleanArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetBooleanArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def SetFloatArrayRegion(arg0: 'float', arg1: int, arg2: 'FloatBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetFloatArrayRegion(float[],int,java.nio.FloatBuffer)"""
        _JNINativeInterface.SetFloatArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def RegisterNatives(arg0: 'Class', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.system.jni.JNINativeInterface.RegisterNatives(java.lang.Class<?>,org.lwjgl.system.jni.JNINativeMethod$Buffer)"""
        return int._wrap(_JNINativeInterface.RegisterNatives(arg0, arg1))

    @staticmethod
    @overload
    def GetByteArrayElements(arg0: bytes, arg1: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.GetByteArrayElements(byte[],java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_JNINativeInterface.GetByteArrayElements(bytes, arg1))

    @staticmethod
    @overload
    def nReleaseLongArrayElements(arg0: 'long', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseLongArrayElements(long[],long,int)"""
        _JNINativeInterface.nReleaseLongArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nSetIntArrayRegion(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetIntArrayRegion(int[],int,int,long)"""
        _JNINativeInterface.nSetIntArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetIntArrayRegion(arg0: 'int', arg1: int, arg2: 'IntBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetIntArrayRegion(int[],int,java.nio.IntBuffer)"""
        _JNINativeInterface.GetIntArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def GetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetDoubleArrayRegion(double[],int,java.nio.DoubleBuffer)"""
        _JNINativeInterface.GetDoubleArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseBooleanArrayElements(arg0: bytes, arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseBooleanArrayElements(byte[],java.nio.ByteBuffer,int)"""
        _JNINativeInterface.ReleaseBooleanArrayElements(bytes, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetStringUTFRegion(arg0: str, arg1: int, arg2: int, arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetStringUTFRegion(java.lang.String,int,int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetStringUTFRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def FromReflectedMethod(arg0: 'Method') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.FromReflectedMethod(java.lang.reflect.Method)"""
        return int._wrap(_JNINativeInterface.FromReflectedMethod(arg0))

    @staticmethod
    @overload
    def nGetDoubleArrayElements(arg0: 'double', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetDoubleArrayElements(double[],long)"""
        return int._wrap(_JNINativeInterface.nGetDoubleArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nDeleteGlobalRef(arg0: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nDeleteGlobalRef(long)"""
        _JNINativeInterface.nDeleteGlobalRef(_long.valueOf(arg0))

 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeInterface
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.nio.IntBuffer as IntBuffer
import java.lang.reflect.Field as Field
import java.nio.LongBuffer as _LongBuffer
_LongBuffer = _LongBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.reflect.Field as _Field
_Field = _Field
import java.nio.DoubleBuffer as _DoubleBuffer
_DoubleBuffer = _DoubleBuffer
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as _object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.lang.reflect.Method as _Method
_Method = _Method
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.nio.Buffer as Buffer
import org.lwjgl.system.jni.JNINativeInterface as _JNINativeInterface
_JNINativeInterface = _JNINativeInterface
import java.nio.ByteBuffer as ByteBuffer
import java.nio.IntBuffer as _IntBuffer
_IntBuffer = _IntBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.reflect.Method as Method
import java.lang.Class as _Class
_Class = _Class
 
class JNINativeInterface():
    """org.lwjgl.system.jni.JNINativeInterface"""
 
    @staticmethod
    def _wrap(java_value: _JNINativeInterface) -> 'JNINativeInterface':
        return JNINativeInterface(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JNINativeInterface):
        """
        Dynamic initializer for JNINativeInterface.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JNINativeInterface__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JNINativeInterface__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nSetByteArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetByteArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nSetByteArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetFloatArrayElements(arg0: 'float', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetFloatArrayElements(float[],long)"""
        return int._wrap(_JNINativeInterface.nGetFloatArrayElements(arg0, _long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def GetVersion() -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.GetVersion()"""
        return int._wrap(_JNINativeInterface.GetVersion())

    @staticmethod
    @overload
    def nReleaseCharArrayElements(arg0: 'char', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseCharArrayElements(char[],long,int)"""
        _JNINativeInterface.nReleaseCharArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nReleaseIntArrayElements(arg0: 'int', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseIntArrayElements(int[],long,int)"""
        _JNINativeInterface.nReleaseIntArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetBooleanArrayElements(arg0: bytes, arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetBooleanArrayElements(byte[],long)"""
        return int._wrap(_JNINativeInterface.nGetBooleanArrayElements(bytes, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetIntArrayElements(arg0: 'int', arg1: 'ByteBuffer') -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.jni.JNINativeInterface.GetIntArrayElements(int[],java.nio.ByteBuffer)"""
        return IntBuffer._wrap(_JNINativeInterface.GetIntArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def ToReflectedField(arg0: 'Class', arg1: int, arg2: bool) -> 'Field':
        """public static java.lang.reflect.Field org.lwjgl.system.jni.JNINativeInterface.ToReflectedField(java.lang.Class<?>,long,boolean)"""
        return Field._wrap(_JNINativeInterface.ToReflectedField(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def NewDirectByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.NewDirectByteBuffer(long,long)"""
        return ByteBuffer._wrap(_JNINativeInterface.NewDirectByteBuffer(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetIntArrayRegion(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetIntArrayRegion(int[],int,int,long)"""
        _JNINativeInterface.nGetIntArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

        @staticmethod
        @overload
        def noop():
            """public static native void org.lwjgl.system.jni.JNINativeInterface.noop()"""
            _JNINativeInterface.noop()

    @staticmethod
    @overload
    def nGetCharArrayRegion(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetCharArrayRegion(char[],int,int,long)"""
        _JNINativeInterface.nGetCharArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetLongArrayElements(arg0: 'long', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetLongArrayElements(long[],long)"""
        return int._wrap(_JNINativeInterface.nGetLongArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nSetShortArrayRegion(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetShortArrayRegion(short[],int,int,long)"""
        _JNINativeInterface.nSetShortArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetCharArrayElements(arg0: 'char', arg1: 'ByteBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.jni.JNINativeInterface.GetCharArrayElements(char[],java.nio.ByteBuffer)"""
        return ShortBuffer._wrap(_JNINativeInterface.GetCharArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nReleaseDoubleArrayElements(arg0: 'double', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseDoubleArrayElements(double[],long,int)"""
        _JNINativeInterface.nReleaseDoubleArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetByteArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetByteArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetByteArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def GetObjectRefType(arg0: object) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.GetObjectRefType(java.lang.Object)"""
        return int._wrap(_JNINativeInterface.GetObjectRefType(arg0))

    @staticmethod
    @overload
    def ReleaseFloatArrayElements(arg0: 'float', arg1: 'FloatBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseFloatArrayElements(float[],java.nio.FloatBuffer,int)"""
        _JNINativeInterface.ReleaseFloatArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetStringRegion(arg0: str, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetStringRegion(java.lang.String,int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetStringRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseDoubleArrayElements(arg0: 'double', arg1: 'DoubleBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseDoubleArrayElements(double[],java.nio.DoubleBuffer,int)"""
        _JNINativeInterface.ReleaseDoubleArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetShortArrayRegion(arg0: 'short', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetShortArrayRegion(short[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.GetShortArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetLongArrayRegion(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetLongArrayRegion(long[],int,int,long)"""
        _JNINativeInterface.nGetLongArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetStringUTFRegion(arg0: str, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetStringUTFRegion(java.lang.String,int,int,long)"""
        _JNINativeInterface.nGetStringUTFRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def NewWeakGlobalRef(arg0: object) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.NewWeakGlobalRef(java.lang.Object)"""
        return int._wrap(_JNINativeInterface.NewWeakGlobalRef(arg0))

    @staticmethod
    @overload
    def ReleaseCharArrayElements(arg0: 'char', arg1: 'ShortBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseCharArrayElements(char[],java.nio.ShortBuffer,int)"""
        _JNINativeInterface.ReleaseCharArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def ReleaseByteArrayElements(arg0: bytes, arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseByteArrayElements(byte[],java.nio.ByteBuffer,int)"""
        _JNINativeInterface.ReleaseByteArrayElements(bytes, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetJavaVM(arg0: int) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.nGetJavaVM(long)"""
        return int._wrap(_JNINativeInterface.nGetJavaVM(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nSetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetBooleanArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nSetBooleanArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nSetLongArrayRegion(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetLongArrayRegion(long[],int,int,long)"""
        _JNINativeInterface.nSetLongArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nToReflectedField(arg0: 'Class', arg1: int, arg2: bool) -> 'Field':
        """public static native java.lang.reflect.Field org.lwjgl.system.jni.JNINativeInterface.nToReflectedField(java.lang.Class<?>,long,boolean)"""
        return Field._wrap(_JNINativeInterface.nToReflectedField(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def GetFloatArrayRegion(arg0: 'float', arg1: int, arg2: 'FloatBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetFloatArrayRegion(float[],int,java.nio.FloatBuffer)"""
        _JNINativeInterface.GetFloatArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nNewDirectByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static native java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.nNewDirectByteBuffer(long,long)"""
        return ByteBuffer._wrap(_JNINativeInterface.nNewDirectByteBuffer(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nReleaseBooleanArrayElements(arg0: bytes, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseBooleanArrayElements(byte[],long,int)"""
        _JNINativeInterface.nReleaseBooleanArrayElements(bytes, _long.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nGetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetBooleanArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nGetBooleanArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def SetCharArrayRegion(arg0: 'char', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetCharArrayRegion(char[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.SetCharArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nReleaseShortArrayElements(arg0: 'short', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseShortArrayElements(short[],long,int)"""
        _JNINativeInterface.nReleaseShortArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def SetShortArrayRegion(arg0: 'short', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetShortArrayRegion(short[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.SetShortArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def SetByteArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetByteArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.SetByteArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def DeleteGlobalRef(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.DeleteGlobalRef(long)"""
        _JNINativeInterface.DeleteGlobalRef(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nGetIntArrayElements(arg0: 'int', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetIntArrayElements(int[],long)"""
        return int._wrap(_JNINativeInterface.nGetIntArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def SetLongArrayRegion(arg0: 'long', arg1: int, arg2: 'LongBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetLongArrayRegion(long[],int,java.nio.LongBuffer)"""
        _JNINativeInterface.SetLongArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def UnregisterNatives(arg0: 'Class') -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.UnregisterNatives(java.lang.Class<?>)"""
        return int._wrap(_JNINativeInterface.UnregisterNatives(arg0))

    @staticmethod
    @overload
    def GetDirectBufferAddress(arg0: 'Buffer') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.GetDirectBufferAddress(java.nio.Buffer)"""
        return int._wrap(_JNINativeInterface.GetDirectBufferAddress(arg0))

    @staticmethod
    @overload
    def nSetCharArrayRegion(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetCharArrayRegion(char[],int,int,long)"""
        _JNINativeInterface.nSetCharArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def ReleaseShortArrayElements(arg0: 'short', arg1: 'ShortBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseShortArrayElements(short[],java.nio.ShortBuffer,int)"""
        _JNINativeInterface.ReleaseShortArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def SetIntArrayRegion(arg0: 'int', arg1: int, arg2: 'IntBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetIntArrayRegion(int[],int,java.nio.IntBuffer)"""
        _JNINativeInterface.SetIntArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetStringRegion(arg0: str, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetStringRegion(java.lang.String,int,int,long)"""
        _JNINativeInterface.nGetStringRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nRegisterNatives(arg0: 'Class', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.nRegisterNatives(java.lang.Class<?>,long,int)"""
        return int._wrap(_JNINativeInterface.nRegisterNatives(arg0, _long.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nReleaseByteArrayElements(arg0: bytes, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseByteArrayElements(byte[],long,int)"""
        _JNINativeInterface.nReleaseByteArrayElements(bytes, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nSetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetDoubleArrayRegion(double[],int,int,long)"""
        _JNINativeInterface.nSetDoubleArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetLongArrayElements(arg0: 'long', arg1: 'ByteBuffer') -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.jni.JNINativeInterface.GetLongArrayElements(long[],java.nio.ByteBuffer)"""
        return LongBuffer._wrap(_JNINativeInterface.GetLongArrayElements(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def GetJavaVM(arg0: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.jni.JNINativeInterface.GetJavaVM(org.lwjgl.PointerBuffer)"""
        return int._wrap(_JNINativeInterface.GetJavaVM(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nGetByteArrayElements(arg0: bytes, arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetByteArrayElements(byte[],long)"""
        return int._wrap(_JNINativeInterface.nGetByteArrayElements(bytes, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def SetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetBooleanArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.SetBooleanArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def FromReflectedField(arg0: 'Field') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.FromReflectedField(java.lang.reflect.Field)"""
        return int._wrap(_JNINativeInterface.FromReflectedField(arg0))

    @staticmethod
    @overload
    def nGetFloatArrayRegion(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetFloatArrayRegion(float[],int,int,long)"""
        _JNINativeInterface.nGetFloatArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def NewGlobalRef(arg0: object) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.NewGlobalRef(java.lang.Object)"""
        return int._wrap(_JNINativeInterface.NewGlobalRef(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def GetCharArrayRegion(arg0: 'char', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetCharArrayRegion(char[],int,java.nio.ShortBuffer)"""
        _JNINativeInterface.GetCharArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nReleaseFloatArrayElements(arg0: 'float', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseFloatArrayElements(float[],long,int)"""
        _JNINativeInterface.nReleaseFloatArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nSetFloatArrayRegion(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetFloatArrayRegion(float[],int,int,long)"""
        _JNINativeInterface.nSetFloatArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetCharArrayElements(arg0: 'char', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetCharArrayElements(char[],long)"""
        return int._wrap(_JNINativeInterface.nGetCharArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def ToReflectedMethod(arg0: 'Class', arg1: int, arg2: bool) -> 'Method':
        """public static java.lang.reflect.Method org.lwjgl.system.jni.JNINativeInterface.ToReflectedMethod(java.lang.Class<?>,long,boolean)"""
        return Method._wrap(_JNINativeInterface.ToReflectedMethod(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def GetFloatArrayElements(arg0: 'float', arg1: 'ByteBuffer') -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.jni.JNINativeInterface.GetFloatArrayElements(float[],java.nio.ByteBuffer)"""
        return FloatBuffer._wrap(_JNINativeInterface.GetFloatArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def GetLongArrayRegion(arg0: 'long', arg1: int, arg2: 'LongBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetLongArrayRegion(long[],int,java.nio.LongBuffer)"""
        _JNINativeInterface.GetLongArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseLongArrayElements(arg0: 'long', arg1: 'LongBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseLongArrayElements(long[],java.nio.LongBuffer,int)"""
        _JNINativeInterface.ReleaseLongArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetByteArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetByteArrayRegion(byte[],int,int,long)"""
        _JNINativeInterface.nGetByteArrayRegion(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetBooleanArrayElements(arg0: bytes, arg1: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.GetBooleanArrayElements(byte[],java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_JNINativeInterface.GetBooleanArrayElements(bytes, arg1))

    @staticmethod
    @overload
    def GetDoubleArrayElements(arg0: 'double', arg1: 'ByteBuffer') -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.jni.JNINativeInterface.GetDoubleArrayElements(double[],java.nio.ByteBuffer)"""
        return DoubleBuffer._wrap(_JNINativeInterface.GetDoubleArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def GetShortArrayElements(arg0: 'short', arg1: 'ByteBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.jni.JNINativeInterface.GetShortArrayElements(short[],java.nio.ByteBuffer)"""
        return ShortBuffer._wrap(_JNINativeInterface.GetShortArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def DeleteWeakGlobalRef(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.DeleteWeakGlobalRef(long)"""
        _JNINativeInterface.DeleteWeakGlobalRef(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nDeleteWeakGlobalRef(arg0: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nDeleteWeakGlobalRef(long)"""
        _JNINativeInterface.nDeleteWeakGlobalRef(_long.valueOf(arg0))

    @staticmethod
    @overload
    def ReleaseIntArrayElements(arg0: 'int', arg1: 'IntBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseIntArrayElements(int[],java.nio.IntBuffer,int)"""
        _JNINativeInterface.ReleaseIntArrayElements(arg0, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetDoubleArrayRegion(double[],int,int,long)"""
        _JNINativeInterface.nGetDoubleArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def SetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetDoubleArrayRegion(double[],int,java.nio.DoubleBuffer)"""
        _JNINativeInterface.SetDoubleArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetShortArrayElements(arg0: 'short', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetShortArrayElements(short[],long)"""
        return int._wrap(_JNINativeInterface.nGetShortArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nToReflectedMethod(arg0: 'Class', arg1: int, arg2: bool) -> 'Method':
        """public static native java.lang.reflect.Method org.lwjgl.system.jni.JNINativeInterface.nToReflectedMethod(java.lang.Class<?>,long,boolean)"""
        return Method._wrap(_JNINativeInterface.nToReflectedMethod(arg0, _long.valueOf(arg1), _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def nGetShortArrayRegion(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetShortArrayRegion(short[],int,int,long)"""
        _JNINativeInterface.nGetShortArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetBooleanArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetBooleanArrayRegion(bytes, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def SetFloatArrayRegion(arg0: 'float', arg1: int, arg2: 'FloatBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetFloatArrayRegion(float[],int,java.nio.FloatBuffer)"""
        _JNINativeInterface.SetFloatArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def RegisterNatives(arg0: 'Class', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.system.jni.JNINativeInterface.RegisterNatives(java.lang.Class<?>,org.lwjgl.system.jni.JNINativeMethod$Buffer)"""
        return int._wrap(_JNINativeInterface.RegisterNatives(arg0, arg1))

    @staticmethod
    @overload
    def GetByteArrayElements(arg0: bytes, arg1: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.GetByteArrayElements(byte[],java.nio.ByteBuffer)"""
        return ByteBuffer._wrap(_JNINativeInterface.GetByteArrayElements(bytes, arg1))

    @staticmethod
    @overload
    def nReleaseLongArrayElements(arg0: 'long', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseLongArrayElements(long[],long,int)"""
        _JNINativeInterface.nReleaseLongArrayElements(arg0, _long.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nSetIntArrayRegion(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetIntArrayRegion(int[],int,int,long)"""
        _JNINativeInterface.nSetIntArrayRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _long.valueOf(arg3))

    @staticmethod
    @overload
    def GetIntArrayRegion(arg0: 'int', arg1: int, arg2: 'IntBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetIntArrayRegion(int[],int,java.nio.IntBuffer)"""
        _JNINativeInterface.GetIntArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def GetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetDoubleArrayRegion(double[],int,java.nio.DoubleBuffer)"""
        _JNINativeInterface.GetDoubleArrayRegion(arg0, _int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseBooleanArrayElements(arg0: bytes, arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseBooleanArrayElements(byte[],java.nio.ByteBuffer,int)"""
        _JNINativeInterface.ReleaseBooleanArrayElements(bytes, arg1, _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetStringUTFRegion(arg0: str, arg1: int, arg2: int, arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetStringUTFRegion(java.lang.String,int,int,java.nio.ByteBuffer)"""
        _JNINativeInterface.GetStringUTFRegion(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def FromReflectedMethod(arg0: 'Method') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.FromReflectedMethod(java.lang.reflect.Method)"""
        return int._wrap(_JNINativeInterface.FromReflectedMethod(arg0))

    @staticmethod
    @overload
    def nGetDoubleArrayElements(arg0: 'double', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetDoubleArrayElements(double[],long)"""
        return int._wrap(_JNINativeInterface.nGetDoubleArrayElements(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nDeleteGlobalRef(arg0: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nDeleteGlobalRef(long)"""
        _JNINativeInterface.nDeleteGlobalRef(_long.valueOf(arg0))

 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeInterface 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeMethod
from pyquantum_helper import import_once as _import_once
import org.lwjgl.system.jni.JNINativeMethod as _JNINativeMethod
_JNINativeMethod = _JNINativeMethod
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.jni.JNINativeMethod as _JNINativeMethod_Buffer
_Buffer = _JNINativeMethod_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class JNINativeMethod():
    """org.lwjgl.system.jni.JNINativeMethod"""
 
    @staticmethod
    def _wrap(java_value: _JNINativeMethod) -> 'JNINativeMethod':
        return JNINativeMethod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JNINativeMethod):
        """
        Dynamic initializer for JNINativeMethod.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JNINativeMethod__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JNINativeMethod__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_JNINativeMethod.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.calloc(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod._wrap(_JNINativeMethod.calloc(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.mallocStack(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod._wrap(_JNINativeMethod.mallocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.callocStack(int)"""
        return Buffer._wrap(_JNINativeMethod.callocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsignatureString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.jni.JNINativeMethod.nsignatureString(long)"""
        return str._wrap(_JNINativeMethod.nsignatureString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.createSafe(long)"""
        return JNINativeMethod._wrap(_JNINativeMethod.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.callocStack(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod._wrap(_JNINativeMethod.callocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.malloc(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod._wrap(_JNINativeMethod.malloc(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: int) -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.create(long)"""
        return JNINativeMethod._wrap(_JNINativeMethod.create(_long.valueOf(arg0)))

    @overload
    def signature(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.signature()"""
        return 'ByteBuffer'._wrap(super(JNINativeMethod, self).signature())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.malloc(int)"""
        return Buffer._wrap(_JNINativeMethod.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nsignature(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nsignature(long,java.nio.ByteBuffer)"""
        _JNINativeMethod.nsignature(_long.valueOf(arg0), arg1)

    @overload
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod.nameString()"""
        return str._wrap(super(JNINativeMethod, self).nameString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.jni.JNINativeMethod.sizeof()"""
        return int._wrap(super(JNINativeMethod, self).sizeof())

    @overload
    def signatureString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod.signatureString()"""
        return str._wrap(super(JNINativeMethod, self).signatureString())

    @staticmethod
    @overload
    def nname(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nname(long,java.nio.ByteBuffer)"""
        _JNINativeMethod.nname(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.createSafe(long,int)"""
        return Buffer._wrap(_JNINativeMethod.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def nsignature(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.nsignature(long)"""
        return ByteBuffer._wrap(_JNINativeMethod.nsignature(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_JNINativeMethod.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.name(java.nio.ByteBuffer)"""
        return 'JNINativeMethod'._wrap(super(_JNINativeMethod, self).name(arg0))

    @staticmethod
    @overload
    def nfnPtr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nfnPtr(long,long)"""
        _JNINativeMethod.nfnPtr(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.mallocStack()"""
        return JNINativeMethod._wrap(_JNINativeMethod.mallocStack())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_JNINativeMethod.malloc(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.create()"""
        return JNINativeMethod._wrap(_JNINativeMethod.create())

    @staticmethod
    @overload
    def callocStack() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.callocStack()"""
        return JNINativeMethod._wrap(_JNINativeMethod.callocStack())

    @staticmethod
    @overload
    def nfnPtr(arg0: int) -> int:
        """public static long org.lwjgl.system.jni.JNINativeMethod.nfnPtr(long)"""
        return int._wrap(_JNINativeMethod.nfnPtr(_long.valueOf(arg0)))

    @overload
    def fnPtr(self) -> int:
        """public long org.lwjgl.system.jni.JNINativeMethod.fnPtr()"""
        return int._wrap(super(JNINativeMethod, self).fnPtr())

    @overload
    def signature(self, arg0: 'ByteBuffer') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.signature(java.nio.ByteBuffer)"""
        return 'JNINativeMethod'._wrap(super(_JNINativeMethod, self).signature(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.calloc(int)"""
        return Buffer._wrap(_JNINativeMethod.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_JNINativeMethod.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.mallocStack(int)"""
        return Buffer._wrap(_JNINativeMethod.mallocStack(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.malloc()"""
        return JNINativeMethod._wrap(_JNINativeMethod.malloc())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.jni.JNINativeMethod(java.nio.ByteBuffer)"""
        val = _JNINativeMethod(arg0)
        self.__wrapper = val

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.name()"""
        return 'ByteBuffer'._wrap(super(JNINativeMethod, self).name())

    @staticmethod
    @overload
    def nname(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.nname(long)"""
        return ByteBuffer._wrap(_JNINativeMethod.nname(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.create(long,int)"""
        return Buffer._wrap(_JNINativeMethod.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.create(int)"""
        return Buffer._wrap(_JNINativeMethod.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.calloc()"""
        return JNINativeMethod._wrap(_JNINativeMethod.calloc())

    @overload
    def set(self, arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: int) -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.set(java.nio.ByteBuffer,java.nio.ByteBuffer,long)"""
        return 'JNINativeMethod'._wrap(super(_JNINativeMethod, self).set(arg0, arg1, _long.valueOf(arg2)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeMethod.validate(long)"""
        _JNINativeMethod.validate(_long.valueOf(arg0))

    @overload
    def fnPtr(self, arg0: int) -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.fnPtr(long)"""
        return 'JNINativeMethod'._wrap(super(_JNINativeMethod, self).fnPtr(_long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'JNINativeMethod') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.set(org.lwjgl.system.jni.JNINativeMethod)"""
        return 'JNINativeMethod'._wrap(super(_JNINativeMethod, self).set(arg0))

    @staticmethod
    @overload
    def nnameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.jni.JNINativeMethod.nnameString(long)"""
        return str._wrap(_JNINativeMethod.nnameString(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeMethod$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.system.jni.JNINativeMethod as _JNINativeMethod_Buffer
_Buffer = _JNINativeMethod_Buffer.Buffer
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.system.jni.JNINativeMethod.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def signature(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod$Buffer.signature()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).signature())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod$Buffer.name(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).name(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def signatureString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod$Buffer.signatureString()"""
        return str._wrap(super(Buffer, self).signatureString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @overload
    def fnPtr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod$Buffer.fnPtr(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).fnPtr(_long.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod$Buffer.nameString()"""
        return str._wrap(super(Buffer, self).nameString())

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod$Buffer.name()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).name())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def signature(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod$Buffer.signature(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).signature(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def fnPtr(self) -> int:
        """public long org.lwjgl.system.jni.JNINativeMethod$Buffer.fnPtr()"""
        return int._wrap(super(Buffer, self).fnPtr())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0))