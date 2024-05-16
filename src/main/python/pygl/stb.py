from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
import org.lwjgl.stb.STBVorbisInfo as __STBVorbisInfo
__STBVorbisInfo = __STBVorbisInfo
import java.nio.IntBuffer as IntBuffer
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import org.lwjgl.stb.STBVorbisComment as __STBVorbisComment
__STBVorbisComment = __STBVorbisComment
from builtins import float
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.lwjgl.stb.STBVorbis as __STBVorbis
__STBVorbis = __STBVorbis
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBVorbis():
    """org.lwjgl.stb.STBVorbis"""
 
    @staticmethod
    def __wrap(java_value: __STBVorbis) -> 'STBVorbis':
        return STBVorbis(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBVorbis):
        """
        Dynamic initializer for STBVorbis.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nstb_vorbis_decode_frame_pushdata(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_frame_pushdata(long,long,int,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def nstb_vorbis_open_filename(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_filename(long,int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_filename(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float_interleaved(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ShortBuffer.__wrap(__STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_stream_length_in_seconds(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBVorbis.stb_vorbis_stream_length_in_seconds(long)"""
        return float.__wrap(__STBVorbis.stb_vorbis_stream_length_in_seconds(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_close(arg0: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_close(long)"""
        __STBVorbis.nstb_vorbis_close(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'ByteBuffer', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.nio.ByteBuffer,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stb_vorbis_seek(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek(long,int)"""
        return bool.__wrap(__STBVorbis.stb_vorbis_seek(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstb_vorbis_open_pushdata(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_pushdata(long,int,int[],int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_pushdata(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short_interleaved(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_stream_length_in_samples(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_stream_length_in_samples(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_stream_length_in_samples(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ShortBuffer.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nstb_vorbis_decode_filename(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_filename(long,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_filename(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_seek_start(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek_start(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_seek_start(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_memory(long,int,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short_interleaved(long,int,short[],int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'CharSequence', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.lang.CharSequence,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_decode_frame_pushdata(arg0: int, arg1: 'ByteBuffer', arg2: 'int', arg3: 'PointerBuffer', arg4: 'int') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_frame_pushdata(long,java.nio.ByteBuffer,int[],org.lwjgl.PointerBuffer,int[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def stb_vorbis_seek_frame(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek_frame(long,int)"""
        return bool.__wrap(__STBVorbis.stb_vorbis_seek_frame(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstb_vorbis_stream_length_in_seconds(arg0: int) -> float:
        """public static native float org.lwjgl.stb.STBVorbis.nstb_vorbis_stream_length_in_seconds(long)"""
        return float.__wrap(__STBVorbis.nstb_vorbis_stream_length_in_seconds(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_seek(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek(long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_seek(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstb_vorbis_get_error(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_error(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_error(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_sample_offset(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_sample_offset(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_sample_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float(long,org.lwjgl.PointerBuffer,int)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_float(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'FloatBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float_interleaved(long,int,java.nio.FloatBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_open_pushdata(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_pushdata(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_pushdata(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_short(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.lang.CharSequence,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_seek_start(arg0: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek_start(long)"""
        return bool.__wrap(__STBVorbis.stb_vorbis_seek_start(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_float(arg0: int, arg1: 'int', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_float(long,int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_float(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,int[],int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'short') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short_interleaved(long,int,short[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_float(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_float(long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_float(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_open_memory(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_memory(long,int,int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stb_vorbis_get_comment(arg0: int, arg1: 'STBVorbisComment') -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbis.stb_vorbis_get_comment(long,org.lwjgl.stb.STBVorbisComment)"""
        return STBVorbisComment.__wrap(__STBVorbis.stb_vorbis_get_comment(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_short(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'ShortBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short_interleaved(long,int,java.nio.ShortBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def stb_vorbis_get_sample_offset(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_sample_offset(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_sample_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_filename(arg0: int, arg1: 'int', arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_filename(long,int[],int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_filename(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_memory(java.nio.ByteBuffer,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_stream_length_in_samples(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_stream_length_in_samples(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_stream_length_in_samples(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_float(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_flush_pushdata(arg0: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_flush_pushdata(long)"""
        __STBVorbis.nstb_vorbis_flush_pushdata(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nstb_vorbis_get_info(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_get_info(long,long)"""
        __STBVorbis.nstb_vorbis_get_info(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short_interleaved(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_float(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_float(long,int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_float(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_get_info(arg0: int, arg1: 'STBVorbisInfo') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbis.stb_vorbis_get_info(long,org.lwjgl.stb.STBVorbisInfo)"""
        return STBVorbisInfo.__wrap(__STBVorbis.stb_vorbis_get_info(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.nio.ByteBuffer,int[],int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'float', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float_interleaved(long,int,float[],int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short_interleaved(long,int,short[],int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_get_error(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_error(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_error(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short(long,org.lwjgl.PointerBuffer,int)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_short(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_close(arg0: int):
        """public static void org.lwjgl.stb.STBVorbis.stb_vorbis_close(long)"""
        __STBVorbis.stb_vorbis_close(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'short') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short_interleaved(long,int,short[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,int[],int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stb_vorbis_get_frame_float(arg0: int, arg1: 'IntBuffer', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_float(long,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_float(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_seek_frame(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek_frame(long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_seek_frame(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'ShortBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short_interleaved(long,int,java.nio.ShortBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'float') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float_interleaved(long,int,float[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstb_vorbis_open_pushdata(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_pushdata(long,int,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_pushdata(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_open_filename(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_filename(long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_filename(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_open_pushdata(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_pushdata(java.nio.ByteBuffer,int[],int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_pushdata(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_decode_frame_pushdata(arg0: int, arg1: 'ByteBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer', arg4: 'IntBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_frame_pushdata(long,java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer,java.nio.IntBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def stb_vorbis_flush_pushdata(arg0: int):
        """public static void org.lwjgl.stb.STBVorbis.stb_vorbis_flush_pushdata(long)"""
        __STBVorbis.stb_vorbis_flush_pushdata(__long.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstb_vorbis_get_comment(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_get_comment(long,long)"""
        __STBVorbis.nstb_vorbis_get_comment(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_file_offset(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_file_offset(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_file_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_file_offset(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_file_offset(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_file_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short(long,org.lwjgl.PointerBuffer,int)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_short(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_open_memory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_memory(long,int,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_memory(java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_decode_frame_pushdata(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: 'int') -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_frame_pushdata(long,long,int,int[],long,int[])"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstb_vorbis_decode_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_memory(long,int,int[],int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

 
 
 
# CLASS: org.lwjgl.stb.STBVorbis
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
import org.lwjgl.stb.STBVorbisInfo as __STBVorbisInfo
__STBVorbisInfo = __STBVorbisInfo
import java.nio.IntBuffer as IntBuffer
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import org.lwjgl.stb.STBVorbisComment as __STBVorbisComment
__STBVorbisComment = __STBVorbisComment
from builtins import float
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.lwjgl.stb.STBVorbis as __STBVorbis
__STBVorbis = __STBVorbis
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBVorbis():
    """org.lwjgl.stb.STBVorbis"""
 
    @staticmethod
    def __wrap(java_value: __STBVorbis) -> 'STBVorbis':
        return STBVorbis(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBVorbis):
        """
        Dynamic initializer for STBVorbis.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nstb_vorbis_decode_frame_pushdata(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_frame_pushdata(long,long,int,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def nstb_vorbis_open_filename(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_filename(long,int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_filename(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float_interleaved(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ShortBuffer.__wrap(__STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_stream_length_in_seconds(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBVorbis.stb_vorbis_stream_length_in_seconds(long)"""
        return float.__wrap(__STBVorbis.stb_vorbis_stream_length_in_seconds(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_close(arg0: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_close(long)"""
        __STBVorbis.nstb_vorbis_close(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'ByteBuffer', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.nio.ByteBuffer,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stb_vorbis_seek(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek(long,int)"""
        return bool.__wrap(__STBVorbis.stb_vorbis_seek(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstb_vorbis_open_pushdata(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_pushdata(long,int,int[],int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_pushdata(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short_interleaved(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_stream_length_in_samples(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_stream_length_in_samples(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_stream_length_in_samples(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ShortBuffer.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nstb_vorbis_decode_filename(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_filename(long,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_filename(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_seek_start(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek_start(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_seek_start(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_memory(long,int,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short_interleaved(long,int,short[],int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'CharSequence', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.lang.CharSequence,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_decode_frame_pushdata(arg0: int, arg1: 'ByteBuffer', arg2: 'int', arg3: 'PointerBuffer', arg4: 'int') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_frame_pushdata(long,java.nio.ByteBuffer,int[],org.lwjgl.PointerBuffer,int[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def stb_vorbis_seek_frame(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek_frame(long,int)"""
        return bool.__wrap(__STBVorbis.stb_vorbis_seek_frame(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstb_vorbis_stream_length_in_seconds(arg0: int) -> float:
        """public static native float org.lwjgl.stb.STBVorbis.nstb_vorbis_stream_length_in_seconds(long)"""
        return float.__wrap(__STBVorbis.nstb_vorbis_stream_length_in_seconds(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_seek(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek(long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_seek(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstb_vorbis_get_error(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_error(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_error(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_sample_offset(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_sample_offset(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_sample_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float(long,org.lwjgl.PointerBuffer,int)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_float(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'FloatBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float_interleaved(long,int,java.nio.FloatBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_open_pushdata(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_pushdata(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_pushdata(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_short(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_filename(java.lang.CharSequence,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_filename(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_seek_start(arg0: int) -> bool:
        """public static boolean org.lwjgl.stb.STBVorbis.stb_vorbis_seek_start(long)"""
        return bool.__wrap(__STBVorbis.stb_vorbis_seek_start(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_float(arg0: int, arg1: 'int', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_float(long,int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_float(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,int[],int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_decode_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'short') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short_interleaved(long,int,short[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_float(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_float(long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_float(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_open_memory(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_memory(long,int,int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stb_vorbis_get_comment(arg0: int, arg1: 'STBVorbisComment') -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbis.stb_vorbis_get_comment(long,org.lwjgl.stb.STBVorbisComment)"""
        return STBVorbisComment.__wrap(__STBVorbis.stb_vorbis_get_comment(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_short(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_short(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_short(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'ShortBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short_interleaved(long,int,java.nio.ShortBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def stb_vorbis_get_sample_offset(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_sample_offset(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_sample_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_decode_filename(arg0: int, arg1: 'int', arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_filename(long,int[],int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_filename(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_memory(java.nio.ByteBuffer,int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def stb_vorbis_stream_length_in_samples(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_stream_length_in_samples(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_stream_length_in_samples(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_float(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_flush_pushdata(arg0: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_flush_pushdata(long)"""
        __STBVorbis.nstb_vorbis_flush_pushdata(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nstb_vorbis_get_info(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_get_info(long,long)"""
        __STBVorbis.nstb_vorbis_get_info(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short_interleaved(long,int,long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_float(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_float(long,int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_float(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_get_info(arg0: int, arg1: 'STBVorbisInfo') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbis.stb_vorbis_get_info(long,org.lwjgl.stb.STBVorbisInfo)"""
        return STBVorbisInfo.__wrap(__STBVorbis.stb_vorbis_get_info(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.nio.ByteBuffer,int[],int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'float', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_samples_float_interleaved(long,int,float[],int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nstb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_frame_short_interleaved(long,int,short[],int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_get_error(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_error(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_error(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short(long,org.lwjgl.PointerBuffer,int)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_short(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_close(arg0: int):
        """public static void org.lwjgl.stb.STBVorbis.stb_vorbis_close(long)"""
        __STBVorbis.stb_vorbis_close(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_vorbis_get_frame_short_interleaved(arg0: int, arg1: int, arg2: 'short') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_short_interleaved(long,int,short[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,int[],int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stb_vorbis_get_frame_float(arg0: int, arg1: 'IntBuffer', arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_frame_float(long,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_frame_float(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_seek_frame(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_seek_frame(long,int)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_seek_frame(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short_interleaved(arg0: int, arg1: int, arg2: 'ShortBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short_interleaved(long,int,java.nio.ShortBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_short_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_float_interleaved(arg0: int, arg1: int, arg2: 'float') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_float_interleaved(long,int,float[])"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_float_interleaved(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstb_vorbis_open_pushdata(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_pushdata(long,int,long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_pushdata(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstb_vorbis_open_filename(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_filename(long,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_filename(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stb_vorbis_open_pushdata(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_pushdata(java.nio.ByteBuffer,int[],int[],org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_pushdata(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_decode_frame_pushdata(arg0: int, arg1: 'ByteBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer', arg4: 'IntBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_frame_pushdata(long,java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer,java.nio.IntBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def stb_vorbis_flush_pushdata(arg0: int):
        """public static void org.lwjgl.stb.STBVorbis.stb_vorbis_flush_pushdata(long)"""
        __STBVorbis.stb_vorbis_flush_pushdata(__long.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstb_vorbis_get_comment(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBVorbis.nstb_vorbis_get_comment(long,long)"""
        __STBVorbis.nstb_vorbis_get_comment(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nstb_vorbis_get_file_offset(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_get_file_offset(long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_get_file_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_get_file_offset(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_file_offset(long)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_file_offset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_vorbis_decode_filename(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_decode_filename(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBVorbis.stb_vorbis_decode_filename(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stb_vorbis_get_samples_short(arg0: int, arg1: 'PointerBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBVorbis.stb_vorbis_get_samples_short(long,org.lwjgl.PointerBuffer,int)"""
        return int.__wrap(__STBVorbis.stb_vorbis_get_samples_short(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstb_vorbis_open_memory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBVorbis.nstb_vorbis_open_memory(long,int,long,long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_open_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stb_vorbis_open_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'STBVorbisAlloc') -> int:
        """public static long org.lwjgl.stb.STBVorbis.stb_vorbis_open_memory(java.nio.ByteBuffer,java.nio.IntBuffer,org.lwjgl.stb.STBVorbisAlloc)"""
        return int.__wrap(__STBVorbis.stb_vorbis_open_memory(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nstb_vorbis_decode_frame_pushdata(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: 'int') -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_frame_pushdata(long,long,int,int[],long,int[])"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_frame_pushdata(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstb_vorbis_decode_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBVorbis.nstb_vorbis_decode_memory(long,int,int[],int[],long)"""
        return int.__wrap(__STBVorbis.nstb_vorbis_decode_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

 
 
 
# CLASS: org.lwjgl.stb.STBVorbis 
 
 
# CLASS: org.lwjgl.stb.STBTTAlignedQuad$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.lwjgl.stb.STBTTAlignedQuad as __STBTTAlignedQuad_Buffer
__Buffer = __STBTTAlignedQuad_Buffer.Buffer
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTAlignedQuad.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def t1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.t1()"""
        return float.__wrap(super(Buffer, self).t1())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def y0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.y0()"""
        return float.__wrap(super(Buffer, self).y0())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def t0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.t0()"""
        return float.__wrap(super(Buffer, self).t0())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def y1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.y1()"""
        return float.__wrap(super(Buffer, self).y1())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTAlignedQuad$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def x1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.x1()"""
        return float.__wrap(super(Buffer, self).x1())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTAlignedQuad$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def s0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.s0()"""
        return float.__wrap(super(Buffer, self).s0())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def x0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.x0()"""
        return float.__wrap(super(Buffer, self).x0())

    @overload
    def s1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad$Buffer.s1()"""
        return float.__wrap(super(Buffer, self).s1())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBTTFontinfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBTTFontinfo as __STBTTFontinfo
__STBTTFontinfo = __STBTTFontinfo
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import org.lwjgl.stb.STBTTFontinfo as __STBTTFontinfo_Buffer
__Buffer = __STBTTFontinfo_Buffer.Buffer
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTFontinfo():
    """org.lwjgl.stb.STBTTFontinfo"""
 
    @staticmethod
    def __wrap(java_value: __STBTTFontinfo) -> 'STBTTFontinfo':
        return STBTTFontinfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTFontinfo):
        """
        Dynamic initializer for STBTTFontinfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTFontinfo.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTFontinfo.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.mallocStack()"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.mallocStack())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTFontinfo.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.calloc(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.malloc(int)"""
        return Buffer.__wrap(__STBTTFontinfo.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTFontinfo.sizeof()"""
        return int.__wrap(super(STBTTFontinfo, self).sizeof())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.createSafe(long)"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.calloc(int)"""
        return Buffer.__wrap(__STBTTFontinfo.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.malloc(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.create()"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.create())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.callocStack(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTFontinfo.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.create(int)"""
        return Buffer.__wrap(__STBTTFontinfo.create(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTFontinfo(java.nio.ByteBuffer)"""
        val = __STBTTFontinfo(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.mallocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTFontinfo.callocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.create(long,int)"""
        return Buffer.__wrap(__STBTTFontinfo.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.callocStack()"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.callocStack())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.calloc()"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.calloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.mallocStack(int)"""
        return Buffer.__wrap(__STBTTFontinfo.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.malloc()"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.malloc())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTFontinfo$Buffer org.lwjgl.stb.STBTTFontinfo.callocStack(int)"""
        return Buffer.__wrap(__STBTTFontinfo.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTFontinfo':
        """public static org.lwjgl.stb.STBTTFontinfo org.lwjgl.stb.STBTTFontinfo.create(long)"""
        return STBTTFontinfo.__wrap(__STBTTFontinfo.create(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.stb.STBDXT
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import org.lwjgl.stb.STBDXT as __STBDXT
__STBDXT = __STBDXT
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBDXT():
    """org.lwjgl.stb.STBDXT"""
 
    @staticmethod
    def __wrap(java_value: __STBDXT) -> 'STBDXT':
        return STBDXT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBDXT):
        """
        Dynamic initializer for STBDXT.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def stb_compress_bc4_block(arg0: 'ByteBuffer', arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBDXT.stb_compress_bc4_block(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        __STBDXT.stb_compress_bc4_block(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nstb_compress_bc4_block(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBDXT.nstb_compress_bc4_block(long,long)"""
        __STBDXT.nstb_compress_bc4_block(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nstb_compress_dxt_block(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBDXT.nstb_compress_dxt_block(long,long,int,int)"""
        __STBDXT.nstb_compress_dxt_block(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stb_compress_bc5_block(arg0: 'ByteBuffer', arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBDXT.stb_compress_bc5_block(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        __STBDXT.stb_compress_bc5_block(arg0, arg1)

    @staticmethod
    @overload
    def stb_compress_dxt_block(arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: bool, arg3: int):
        """public static void org.lwjgl.stb.STBDXT.stb_compress_dxt_block(java.nio.ByteBuffer,java.nio.ByteBuffer,boolean,int)"""
        __STBDXT.stb_compress_dxt_block(arg0, arg1, __boolean.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def nstb_compress_bc5_block(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBDXT.nstb_compress_bc5_block(long,long)"""
        __STBDXT.nstb_compress_bc5_block(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.lwjgl.stb.STBRPContext as __STBRPContext
__STBRPContext = __STBRPContext
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBRPNode as __STBRPNode_Buffer
__Buffer = __STBRPNode_Buffer.Buffer
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.stb.STBTTPackContext as __STBTTPackContext_Buffer
__Buffer = __STBTTPackContext_Buffer.Buffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import org.lwjgl.stb.STBTTPackContext as __STBTTPackContext
__STBTTPackContext = __STBTTPackContext
from builtins import int
 
class STBTTPackContext():
    """org.lwjgl.stb.STBTTPackContext"""
 
    @staticmethod
    def __wrap(java_value: __STBTTPackContext) -> 'STBTTPackContext':
        return STBTTPackContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTPackContext):
        """
        Dynamic initializer for STBTTPackContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.malloc()"""
        return STBTTPackContext.__wrap(__STBTTPackContext.malloc())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext.__wrap(__STBTTPackContext.mallocStack(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def pack_info(self) -> 'STBRPContext':
        """public org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBTTPackContext.pack_info()"""
        return 'STBRPContext'.__wrap(super(STBTTPackContext, self).pack_info())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.create(int)"""
        return Buffer.__wrap(__STBTTPackContext.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext.__wrap(__STBTTPackContext.calloc(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nskip_missing(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nskip_missing(long)"""
        return int.__wrap(__STBTTPackContext.nskip_missing(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackContext.mallocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def v_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.v_oversample()"""
        return int.__wrap(super(STBTTPackContext, self).v_oversample())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext.__wrap(__STBTTPackContext.malloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.mallocStack(int)"""
        return Buffer.__wrap(__STBTTPackContext.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nheight(long)"""
        return int.__wrap(__STBTTPackContext.nheight(__long.valueOf(arg0)))

    @overload
    def skip_missing(self) -> bool:
        """public boolean org.lwjgl.stb.STBTTPackContext.skip_missing()"""
        return bool.__wrap(super(STBTTPackContext, self).skip_missing())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackContext.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def stride_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.stride_in_bytes()"""
        return int.__wrap(super(STBTTPackContext, self).stride_in_bytes())

    @overload
    def width(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.width()"""
        return int.__wrap(super(STBTTPackContext, self).width())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nnodes(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBTTPackContext.nnodes(long,int)"""
        return Buffer.__wrap(__STBTTPackContext.nnodes(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.sizeof()"""
        return int.__wrap(super(STBTTPackContext, self).sizeof())

    @staticmethod
    @overload
    def npack_info(arg0: int) -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBTTPackContext.npack_info(long)"""
        return STBRPContext.__wrap(__STBTTPackContext.npack_info(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstride_in_bytes(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nstride_in_bytes(long)"""
        return int.__wrap(__STBTTPackContext.nstride_in_bytes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nv_oversample(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nv_oversample(long)"""
        return int.__wrap(__STBTTPackContext.nv_oversample(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.mallocStack()"""
        return STBTTPackContext.__wrap(__STBTTPackContext.mallocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.create(long)"""
        return STBTTPackContext.__wrap(__STBTTPackContext.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.calloc()"""
        return STBTTPackContext.__wrap(__STBTTPackContext.calloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTPackContext.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.create(long,int)"""
        return Buffer.__wrap(__STBTTPackContext.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nh_oversample(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nh_oversample(long)"""
        return int.__wrap(__STBTTPackContext.nh_oversample(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackContext(java.nio.ByteBuffer)"""
        val = __STBTTPackContext(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackContext.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nuser_allocator_context(arg0: int) -> int:
        """public static long org.lwjgl.stb.STBTTPackContext.nuser_allocator_context(long)"""
        return int.__wrap(__STBTTPackContext.nuser_allocator_context(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackContext.malloc(__int.valueOf(arg0), arg1))

    @overload
    def height(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.height()"""
        return int.__wrap(super(STBTTPackContext, self).height())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.createSafe(long)"""
        return STBTTPackContext.__wrap(__STBTTPackContext.createSafe(__long.valueOf(arg0)))

    @overload
    def h_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.h_oversample()"""
        return int.__wrap(super(STBTTPackContext, self).h_oversample())

    @overload
    def nodes(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBTTPackContext.nodes(int)"""
        return 'Buffer'.__wrap(super(__STBTTPackContext, self).nodes(__int.valueOf(arg0)))

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTPackContext.pixels(int)"""
        return 'ByteBuffer'.__wrap(super(__STBTTPackContext, self).pixels(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTTPackContext.npixels(long,int)"""
        return ByteBuffer.__wrap(__STBTTPackContext.npixels(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.callocStack()"""
        return STBTTPackContext.__wrap(__STBTTPackContext.callocStack())

    @staticmethod
    @overload
    def npadding(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.npadding(long)"""
        return int.__wrap(__STBTTPackContext.npadding(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create() -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.create()"""
        return STBTTPackContext.__wrap(__STBTTPackContext.create())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTPackContext':
        """public static org.lwjgl.stb.STBTTPackContext org.lwjgl.stb.STBTTPackContext.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackContext.__wrap(__STBTTPackContext.callocStack(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.calloc(int)"""
        return Buffer.__wrap(__STBTTPackContext.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def user_allocator_context(self) -> int:
        """public long org.lwjgl.stb.STBTTPackContext.user_allocator_context()"""
        return int.__wrap(super(STBTTPackContext, self).user_allocator_context())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackContext.nwidth(long)"""
        return int.__wrap(__STBTTPackContext.nwidth(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.callocStack(int)"""
        return Buffer.__wrap(__STBTTPackContext.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackContext$Buffer org.lwjgl.stb.STBTTPackContext.malloc(int)"""
        return Buffer.__wrap(__STBTTPackContext.malloc(__int.valueOf(arg0)))

    @overload
    def padding(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext.padding()"""
        return int.__wrap(super(STBTTPackContext, self).padding()) 
 
 
# CLASS: org.lwjgl.stb.STBISkipCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
import org.lwjgl.stb.STBISkipCallbackI as __STBISkipCallbackI
__STBISkipCallbackI = __STBISkipCallbackI
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class STBISkipCallbackI(ABC):
    """org.lwjgl.stb.STBISkipCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __STBISkipCallbackI) -> 'STBISkipCallbackI':
        return STBISkipCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBISkipCallbackI):
        """
        Dynamic initializer for STBISkipCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBISkipCallbackI.callback(long,long)"""
        super(__STBISkipCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.stb.STBISkipCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBISkipCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBISkipCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBTTBakedChar
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.stb.STBTTBakedChar as __STBTTBakedChar
__STBTTBakedChar = __STBTTBakedChar
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBTTBakedChar as __STBTTBakedChar_Buffer
__Buffer = __STBTTBakedChar_Buffer.Buffer
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTBakedChar():
    """org.lwjgl.stb.STBTTBakedChar"""
 
    @staticmethod
    def __wrap(java_value: __STBTTBakedChar) -> 'STBTTBakedChar':
        return STBTTBakedChar(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTBakedChar):
        """
        Dynamic initializer for STBTTBakedChar.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBakedChar(java.nio.ByteBuffer)"""
        val = __STBTTBakedChar(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar.yoff()"""
        return float.__wrap(super(STBTTBakedChar, self).yoff())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.callocStack(int)"""
        return Buffer.__wrap(__STBTTBakedChar.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nyoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTBakedChar.nyoff(long)"""
        return float.__wrap(__STBTTBakedChar.nyoff(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.malloc()"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.malloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.y0()"""
        return int.__wrap(super(STBTTBakedChar, self).y0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.x1()"""
        return int.__wrap(super(STBTTBakedChar, self).x1())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.malloc(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.malloc(int)"""
        return Buffer.__wrap(__STBTTBakedChar.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBakedChar.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.callocStack(arg0))

    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar.xoff()"""
        return float.__wrap(super(STBTTBakedChar, self).xoff())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTBakedChar.sizeof()"""
        return int.__wrap(super(STBTTBakedChar, self).sizeof())

    @overload
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.x0()"""
        return int.__wrap(super(STBTTBakedChar, self).x0())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTBakedChar.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar.y1()"""
        return int.__wrap(super(STBTTBakedChar, self).y1())

    @staticmethod
    @overload
    def callocStack() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.callocStack()"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.callocStack())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nx1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.nx1(long)"""
        return int.__wrap(__STBTTBakedChar.nx1(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def ny0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.ny0(long)"""
        return int.__wrap(__STBTTBakedChar.ny0(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nxadvance(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTBakedChar.nxadvance(long)"""
        return float.__wrap(__STBTTBakedChar.nxadvance(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBakedChar.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.create(long)"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.create(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def calloc() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.calloc()"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.calloc())

    @staticmethod
    @overload
    def ny1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.ny1(long)"""
        return int.__wrap(__STBTTBakedChar.ny1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.mallocStack()"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.mallocStack())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.mallocStack(arg0))

    @staticmethod
    @overload
    def create() -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.create()"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.create())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nxoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTBakedChar.nxoff(long)"""
        return float.__wrap(__STBTTBakedChar.nxoff(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.create(long,int)"""
        return Buffer.__wrap(__STBTTBakedChar.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.createSafe(long)"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.mallocStack(int)"""
        return Buffer.__wrap(__STBTTBakedChar.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.create(int)"""
        return Buffer.__wrap(__STBTTBakedChar.create(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nx0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTBakedChar.nx0(long)"""
        return int.__wrap(__STBTTBakedChar.nx0(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar.xadvance()"""
        return float.__wrap(super(STBTTBakedChar, self).xadvance())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBakedChar.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBakedChar.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBakedChar$Buffer org.lwjgl.stb.STBTTBakedChar.calloc(int)"""
        return Buffer.__wrap(__STBTTBakedChar.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTBakedChar':
        """public static org.lwjgl.stb.STBTTBakedChar org.lwjgl.stb.STBTTBakedChar.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBakedChar.__wrap(__STBTTBakedChar.calloc(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackedchar$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.Float as __float
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.stb.STBTTPackedchar as __STBTTPackedchar_Buffer
__Buffer = __STBTTPackedchar_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTPackedchar.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def y1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.y1(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).y1(__short.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.y0()"""
        return int.__wrap(super(Buffer, self).y0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.yoff()"""
        return float.__wrap(super(Buffer, self).yoff())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackedchar$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def y0(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.y0(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).y0(__short.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.x0()"""
        return int.__wrap(super(Buffer, self).x0())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def xoff2(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.xoff2(float)"""
        return 'Buffer'.__wrap(super(__Buffer, self).xoff2(__float.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.y1()"""
        return int.__wrap(super(Buffer, self).y1())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def yoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.yoff2()"""
        return float.__wrap(super(Buffer, self).yoff2())

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def xoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.xoff2()"""
        return float.__wrap(super(Buffer, self).xoff2())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.xadvance()"""
        return float.__wrap(super(Buffer, self).xadvance())

    @overload
    def xadvance(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.xadvance(float)"""
        return 'Buffer'.__wrap(super(__Buffer, self).xadvance(__float.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def x0(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.x0(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).x0(__short.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def yoff2(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.yoff2(float)"""
        return 'Buffer'.__wrap(super(__Buffer, self).yoff2(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTPackedchar$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def x1(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.x1(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).x1(__short.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar$Buffer.x1()"""
        return int.__wrap(super(Buffer, self).x1())

    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar$Buffer.xoff()"""
        return float.__wrap(super(Buffer, self).xoff())

    @overload
    def xoff(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.xoff(float)"""
        return 'Buffer'.__wrap(super(__Buffer, self).xoff(__float.valueOf(arg0)))

    @overload
    def yoff(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar$Buffer.yoff(float)"""
        return 'Buffer'.__wrap(super(__Buffer, self).yoff(__float.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBRPRect$Buffer
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.lwjgl.stb.STBRPRect as __STBRPRect_Buffer
__Buffer = __STBRPRect_Buffer.Buffer
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBRPRect.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.y()"""
        return int.__wrap(super(Buffer, self).y())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBRPRect$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def w(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.w()"""
        return int.__wrap(super(Buffer, self).w())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPRect$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def y(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.y(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).y(__int.valueOf(arg0)))

    @overload
    def id(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.id(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).id(__int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def h(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.h()"""
        return int.__wrap(super(Buffer, self).h())

    @overload
    def w(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.w(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).w(__int.valueOf(arg0)))

    @overload
    def was_packed(self, arg0: bool) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.was_packed(boolean)"""
        return 'Buffer'.__wrap(super(__Buffer, self).was_packed(__boolean.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def id(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.id()"""
        return int.__wrap(super(Buffer, self).id())

    @overload
    def was_packed(self) -> bool:
        """public boolean org.lwjgl.stb.STBRPRect$Buffer.was_packed()"""
        return bool.__wrap(super(Buffer, self).was_packed())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPRect$Buffer.x()"""
        return int.__wrap(super(Buffer, self).x())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def x(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.x(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).x(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def h(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect$Buffer.h(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).h(__int.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBImageResize
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.stb.STBImageResize as __STBImageResize
__STBImageResize = __STBImageResize
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBImageResize():
    """org.lwjgl.stb.STBImageResize"""
 
    @staticmethod
    def __wrap(java_value: __STBImageResize) -> 'STBImageResize':
        return STBImageResize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBImageResize):
        """
        Dynamic initializer for STBImageResize.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def stbir_resize_subpixel(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: float, arg18: float, arg19: float, arg20: float) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_subpixel(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int,int,int,int,float,float,float,float)"""
        return bool.__wrap(__STBImageResize.stbir_resize_subpixel(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __float.valueOf(arg17), __float.valueOf(arg18), __float.valueOf(arg19), __float.valueOf(arg20)))

    @staticmethod
    @overload
    def stbir_resize_uint16_generic(arg0: 'ShortBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ShortBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint16_generic(java.nio.ShortBuffer,int,int,int,java.nio.ShortBuffer,int,int,int,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_uint16_generic(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13)))

    @staticmethod
    @overload
    def nstbir_resize_region(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: float, arg19: float, arg20: float, arg21: float) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_region(long,int,int,int,long,int,int,int,int,int,int,int,int,int,int,int,int,long,float,float,float,float)"""
        return int.__wrap(__STBImageResize.nstbir_resize_region(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __long.valueOf(arg17), __float.valueOf(arg18), __float.valueOf(arg19), __float.valueOf(arg20), __float.valueOf(arg21)))

    @staticmethod
    @overload
    def stbir_resize_float_generic(arg0: 'FloatBuffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float_generic(java.nio.FloatBuffer,int,int,int,java.nio.FloatBuffer,int,int,int,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_float_generic(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13)))

    @staticmethod
    @overload
    def nstbir_resize(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize(long,int,int,int,long,int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        return int.__wrap(__STBImageResize.nstbir_resize(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __long.valueOf(arg17)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stbir_resize_uint8_srgb_edgemode(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8_srgb_edgemode(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_uint8_srgb_edgemode(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11)))

    @staticmethod
    @overload
    def nstbir_resize_float_generic(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float_generic(float[],int,int,int,float[],int,int,int,int,int,int,int,int,int,long)"""
        return int.__wrap(__STBImageResize.nstbir_resize_float_generic(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def nstbir_resize_uint8_srgb_edgemode(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8_srgb_edgemode(long,int,int,int,long,int,int,int,int,int,int,int)"""
        return int.__wrap(__STBImageResize.nstbir_resize_uint8_srgb_edgemode(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11)))

    @staticmethod
    @overload
    def stbir_resize_uint8(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_uint8(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8)))

    @staticmethod
    @overload
    def stbir_resize_uint8_srgb(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8_srgb(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_uint8_srgb(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10)))

    @staticmethod
    @overload
    def stbir_resize_uint16_generic(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint16_generic(short[],int,int,int,short[],int,int,int,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_uint16_generic(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stbir_resize(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16)))

    @staticmethod
    @overload
    def nstbir_resize_uint8(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8(long,int,int,int,long,int,int,int,int)"""
        return int.__wrap(__STBImageResize.nstbir_resize_uint8(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stbir_resize_uint8_generic(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_uint8_generic(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_uint8_generic(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13)))

    @staticmethod
    @overload
    def nstbir_resize_uint16_generic(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint16_generic(short[],int,int,int,short[],int,int,int,int,int,int,int,int,int,long)"""
        return int.__wrap(__STBImageResize.nstbir_resize_uint16_generic(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __long.valueOf(arg14)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def stbir_resize_region(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: float, arg18: float, arg19: float, arg20: float) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_region(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int,int,int,int,int,int,int,int,int,int,int,int,float,float,float,float)"""
        return bool.__wrap(__STBImageResize.stbir_resize_region(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __float.valueOf(arg17), __float.valueOf(arg18), __float.valueOf(arg19), __float.valueOf(arg20)))

    @staticmethod
    @overload
    def nstbir_resize_uint8_srgb(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8_srgb(long,int,int,int,long,int,int,int,int,int,int)"""
        return int.__wrap(__STBImageResize.nstbir_resize_uint8_srgb(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10)))

    @staticmethod
    @overload
    def nstbir_resize_uint16_generic(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint16_generic(long,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int.__wrap(__STBImageResize.nstbir_resize_uint16_generic(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __long.valueOf(arg14)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstbir_resize_float_generic(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float_generic(long,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int.__wrap(__STBImageResize.nstbir_resize_float_generic(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def stbir_resize_float(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float(float[],int,int,int,float[],int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_float(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8)))

    @staticmethod
    @overload
    def nstbir_resize_float(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float(long,int,int,int,long,int,int,int,int)"""
        return int.__wrap(__STBImageResize.nstbir_resize_float(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstbir_resize_uint8_generic(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_uint8_generic(long,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int.__wrap(__STBImageResize.nstbir_resize_uint8_generic(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def nstbir_resize_subpixel(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: float, arg19: float, arg20: float, arg21: float) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_subpixel(long,int,int,int,long,int,int,int,int,int,int,int,int,int,int,int,int,long,float,float,float,float)"""
        return int.__wrap(__STBImageResize.nstbir_resize_subpixel(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __long.valueOf(arg17), __float.valueOf(arg18), __float.valueOf(arg19), __float.valueOf(arg20), __float.valueOf(arg21)))

    @staticmethod
    @overload
    def stbir_resize_float_generic(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float_generic(float[],int,int,int,float[],int,int,int,int,int,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_float_generic(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nstbir_resize_float(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBImageResize.nstbir_resize_float(float[],int,int,int,float[],int,int,int,int)"""
        return int.__wrap(__STBImageResize.nstbir_resize_float(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8)))

    @staticmethod
    @overload
    def stbir_resize_float(arg0: 'FloatBuffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageResize.stbir_resize_float(java.nio.FloatBuffer,int,int,int,java.nio.FloatBuffer,int,int,int,int)"""
        return bool.__wrap(__STBImageResize.stbir_resize_float(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))) 
 
 
# CLASS: org.lwjgl.stb.STBImage
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.stb.STBImage as __STBImage
__STBImage = __STBImage
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBImage():
    """org.lwjgl.stb.STBImage"""
 
    @staticmethod
    def __wrap(java_value: __STBImage) -> 'STBImage':
        return STBImage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBImage):
        """
        Dynamic initializer for STBImage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stbi_load(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.lang.CharSequence,int[],int[],int[],int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_load_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[],int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_loadf(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf(long,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_loadf(__long.valueOf(arg0), arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_zlib_decode_noheader_buffer(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBImage.stbi_zlib_decode_noheader_buffer(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int.__wrap(__STBImage.stbi_zlib_decode_noheader_buffer(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stbi_zlib_decode_malloc_guesssize(arg0: 'ByteBuffer', arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_malloc_guesssize(java.nio.ByteBuffer,int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_zlib_decode_malloc_guesssize(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbi_convert_iphone_png_to_rgb_thread(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_convert_iphone_png_to_rgb_thread(boolean)"""
        __STBImage.stbi_convert_iphone_png_to_rgb_thread(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_loadf_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_convert_iphone_png_to_rgb_thread(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_convert_iphone_png_to_rgb_thread(int)"""
        __STBImage.nstbi_convert_iphone_png_to_rgb_thread(__int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_convert_iphone_png_to_rgb(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_convert_iphone_png_to_rgb(boolean)"""
        __STBImage.stbi_convert_iphone_png_to_rgb(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def stbi_load_gif_from_memory(arg0: 'ByteBuffer', arg1: 'PointerBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_gif_from_memory(java.nio.ByteBuffer,org.lwjgl.PointerBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load_gif_from_memory(arg0, arg1, arg2, arg3, arg4, arg5, __int.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_malloc_guesssize_headerflag(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_malloc_guesssize_headerflag(long,int,int,long,int)"""
        return int.__wrap(__STBImage.nstbi_zlib_decode_malloc_guesssize_headerflag(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_info(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.nio.ByteBuffer,int[],int[],int[])"""
        return bool.__wrap(__STBImage.stbi_info(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbi_load_gif_from_memory(arg0: 'ByteBuffer', arg1: 'PointerBuffer', arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_gif_from_memory(java.nio.ByteBuffer,org.lwjgl.PointerBuffer,int[],int[],int[],int[],int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load_gif_from_memory(arg0, arg1, arg2, arg3, arg4, arg5, __int.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbi_load_16_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_memory(long,int,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_load_16_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_is_hdr_from_memory(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_hdr_from_memory(long,int)"""
        return int.__wrap(__STBImage.nstbi_is_hdr_from_memory(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbi_loadf(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf(long,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_loadf(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_load_16_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16_from_memory(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_load_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_memory(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load_from_memory(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_is_16_bit(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit(java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImage.stbi_is_16_bit(arg0))

    @staticmethod
    @overload
    def nstbi_load_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_callbacks(long,long,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_load_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_loadf_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf_from_memory(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_set_flip_vertically_on_load(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_set_flip_vertically_on_load(boolean)"""
        __STBImage.stbi_set_flip_vertically_on_load(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_load_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_is_hdr(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_hdr(long)"""
        return int.__wrap(__STBImage.nstbi_is_hdr(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stbi_ldr_to_hdr_scale(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_ldr_to_hdr_scale(float)"""
        __STBImage.stbi_ldr_to_hdr_scale(__float.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_convert_iphone_png_to_rgb(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_convert_iphone_png_to_rgb(int)"""
        __STBImage.nstbi_convert_iphone_png_to_rgb(__int.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_load_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_memory(long,int,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_load_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def stbi_is_16_bit_from_memory(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit_from_memory(java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImage.stbi_is_16_bit_from_memory(arg0))

    @staticmethod
    @overload
    def nstbi_loadf_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_memory(long,int,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_loadf_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_failure_reason() -> str:
        """public static java.lang.String org.lwjgl.stb.STBImage.stbi_failure_reason()"""
        return str.__wrap(__STBImage.stbi_failure_reason())

    @staticmethod
    @overload
    def nstbi_info_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int') -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_callbacks(long,long,int[],int[],int[])"""
        return int.__wrap(__STBImage.nstbi_info_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def stbi_info_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[])"""
        return bool.__wrap(__STBImage.stbi_info_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def stbi_load_16_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_zlib_decode_malloc_guesssize_headerflag(arg0: 'ByteBuffer', arg1: int, arg2: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_malloc_guesssize_headerflag(java.nio.ByteBuffer,int,boolean)"""
        return ByteBuffer.__wrap(__STBImage.stbi_zlib_decode_malloc_guesssize_headerflag(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbi_info_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_callbacks(long,long,long,long,long)"""
        return int.__wrap(__STBImage.nstbi_info_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_hdr_to_ldr_gamma(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_hdr_to_ldr_gamma(float)"""
        __STBImage.stbi_hdr_to_ldr_gamma(__float.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nstbi_load_16(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16(long,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_load_16(__long.valueOf(arg0), arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_loadf_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[],int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_info_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_memory(java.nio.ByteBuffer,int[],int[],int[])"""
        return bool.__wrap(__STBImage.stbi_info_from_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbi_load_gif_from_memory(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_gif_from_memory(long,int,long,int[],int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_load_gif_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, arg5, arg6, __int.valueOf(arg7)))

    @staticmethod
    @overload
    def nstbi_set_flip_vertically_on_load(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_set_flip_vertically_on_load(int)"""
        __STBImage.nstbi_set_flip_vertically_on_load(__int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_load(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_load_gif_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_gif_from_memory(long,int,long,long,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_load_gif_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7)))

    @staticmethod
    @overload
    def nstbi_is_hdr_from_callbacks(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_hdr_from_callbacks(long,long)"""
        return int.__wrap(__STBImage.nstbi_is_hdr_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def stbi_zlib_decode_noheader_malloc(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_noheader_malloc(java.nio.ByteBuffer)"""
        return ByteBuffer.__wrap(__STBImage.stbi_zlib_decode_noheader_malloc(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_info_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool.__wrap(__STBImage.stbi_info_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def nstbi_zlib_decode_noheader_buffer(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_zlib_decode_noheader_buffer(long,int,long,int)"""
        return int.__wrap(__STBImage.nstbi_zlib_decode_noheader_buffer(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stbi_set_unpremultiply_on_load(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_set_unpremultiply_on_load(boolean)"""
        __STBImage.stbi_set_unpremultiply_on_load(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_zlib_decode_buffer(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBImage.stbi_zlib_decode_buffer(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int.__wrap(__STBImage.stbi_zlib_decode_buffer(arg0, arg1))

    @staticmethod
    @overload
    def stbi_load(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_image_free(arg0: 'ShortBuffer'):
        """public static void org.lwjgl.stb.STBImage.stbi_image_free(java.nio.ShortBuffer)"""
        __STBImage.stbi_image_free(arg0)

    @staticmethod
    @overload
    def stbi_info(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.lang.CharSequence,int[],int[],int[])"""
        return bool.__wrap(__STBImage.stbi_info(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbi_info_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int') -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_memory(long,int,int[],int[],int[])"""
        return int.__wrap(__STBImage.nstbi_info_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.lang.CharSequence,int[],int[],int[],int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_malloc_guesssize(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_malloc_guesssize(long,int,int,long)"""
        return int.__wrap(__STBImage.nstbi_zlib_decode_malloc_guesssize(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stbi_load_16_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_memory(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16_from_memory(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_set_unpremultiply_on_load_thread(arg0: bool):
        """public static void org.lwjgl.stb.STBImage.stbi_set_unpremultiply_on_load_thread(boolean)"""
        __STBImage.stbi_set_unpremultiply_on_load_thread(__boolean.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_hdr_to_ldr_scale(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_hdr_to_ldr_scale(float)"""
        __STBImage.stbi_hdr_to_ldr_scale(__float.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_is_hdr(arg0: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr(java.lang.CharSequence)"""
        return bool.__wrap(__STBImage.stbi_is_hdr(arg0))

    @staticmethod
    @overload
    def stbi_is_hdr(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr(java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImage.stbi_is_hdr(arg0))

    @staticmethod
    @overload
    def stbi_info_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool.__wrap(__STBImage.stbi_info_from_memory(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbi_load_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_callbacks(long,long,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_load_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_noheader_malloc(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_noheader_malloc(long,int,long)"""
        return int.__wrap(__STBImage.nstbi_zlib_decode_noheader_malloc(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'CharSequence', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.lang.CharSequence,int[],int[],int[],int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_is_hdr_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long)"""
        return bool.__wrap(__STBImage.stbi_is_hdr_from_callbacks(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def stbi_load_16_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long,int[],int[],int[],int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16_from_callbacks(arg0, __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stbi_load(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_loadf(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_loadf_from_memory(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.stb.STBImage.stbi_loadf_from_memory(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return FloatBuffer.__wrap(__STBImage.stbi_loadf_from_memory(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_is_16_bit_from_callbacks(arg0: 'STBIIOCallbacks', arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit_from_callbacks(org.lwjgl.stb.STBIIOCallbacks,long)"""
        return bool.__wrap(__STBImage.stbi_is_16_bit_from_callbacks(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbi_load(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load(long,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_load(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbi_is_16_bit(arg0: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_16_bit(java.lang.CharSequence)"""
        return bool.__wrap(__STBImage.stbi_is_16_bit(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstbi_set_unpremultiply_on_load(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_set_unpremultiply_on_load(int)"""
        __STBImage.nstbi_set_unpremultiply_on_load(__int.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_info(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int') -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info(long,int[],int[],int[])"""
        return int.__wrap(__STBImage.nstbi_info(__long.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbi_set_flip_vertically_on_load_thread(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.stbi_set_flip_vertically_on_load_thread(int)"""
        __STBImage.stbi_set_flip_vertically_on_load_thread(__int.valueOf(arg0))

    @staticmethod
    @overload
    def stbi_ldr_to_hdr_gamma(arg0: float):
        """public static native void org.lwjgl.stb.STBImage.stbi_ldr_to_hdr_gamma(float)"""
        __STBImage.stbi_ldr_to_hdr_gamma(__float.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_info(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info(long,long,long,long)"""
        return int.__wrap(__STBImage.nstbi_info(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stbi_image_free(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBImage.stbi_image_free(java.nio.ByteBuffer)"""
        __STBImage.stbi_image_free(arg0)

    @staticmethod
    @overload
    def nstbi_load_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_from_memory(long,int,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_load_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_load_16(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16(long,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_load_16(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_is_16_bit_from_memory(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_16_bit_from_memory(long,int)"""
        return int.__wrap(__STBImage.nstbi_is_16_bit_from_memory(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbi_load_16_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_memory(long,int,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_load_16_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_zlib_decode_buffer(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_zlib_decode_buffer(long,int,long,int)"""
        return int.__wrap(__STBImage.nstbi_zlib_decode_buffer(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stbi_image_free(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.stb.STBImage.stbi_image_free(java.nio.FloatBuffer)"""
        __STBImage.stbi_image_free(arg0)

    @staticmethod
    @overload
    def stbi_info(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool.__wrap(__STBImage.stbi_info(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stbi_load_from_memory(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_load_from_memory(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ByteBuffer.__wrap(__STBImage.stbi_load_from_memory(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_loadf_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_callbacks(long,long,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_loadf_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_zlib_decode_malloc(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBImage.stbi_zlib_decode_malloc(java.nio.ByteBuffer)"""
        return ByteBuffer.__wrap(__STBImage.stbi_zlib_decode_malloc(arg0))

    @staticmethod
    @overload
    def nstbi_zlib_decode_malloc(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_zlib_decode_malloc(long,int,long)"""
        return int.__wrap(__STBImage.nstbi_zlib_decode_malloc(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'ByteBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.nio.ByteBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_is_16_bit(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_16_bit(long)"""
        return int.__wrap(__STBImage.nstbi_is_16_bit(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstbi_load_16_from_callbacks(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_callbacks(long,long,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_load_16_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_is_hdr_from_memory(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_is_hdr_from_memory(java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImage.stbi_is_hdr_from_memory(arg0))

    @staticmethod
    @overload
    def nstbi_info_from_memory(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_info_from_memory(long,int,long,long,long)"""
        return int.__wrap(__STBImage.nstbi_info_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_loadf_from_memory(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_memory(long,int,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_loadf_from_memory(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_load_16(arg0: 'ByteBuffer', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.stb.STBImage.stbi_load_16(java.nio.ByteBuffer,int[],int[],int[],int)"""
        return ShortBuffer.__wrap(__STBImage.stbi_load_16(arg0, arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_failure_reason() -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_failure_reason()"""
        return int.__wrap(__STBImage.nstbi_failure_reason())

    @staticmethod
    @overload
    def nstbi_load_16_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load_16_from_callbacks(long,long,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_load_16_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_set_unpremultiply_on_load_thread(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_set_unpremultiply_on_load_thread(int)"""
        __STBImage.nstbi_set_unpremultiply_on_load_thread(__int.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_is_16_bit_from_callbacks(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBImage.nstbi_is_16_bit_from_callbacks(long,long)"""
        return int.__wrap(__STBImage.nstbi_is_16_bit_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbi_image_free(arg0: int):
        """public static native void org.lwjgl.stb.STBImage.nstbi_image_free(long)"""
        __STBImage.nstbi_image_free(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstbi_load(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_load(long,int[],int[],int[],int)"""
        return int.__wrap(__STBImage.nstbi_load(__long.valueOf(arg0), arg1, arg2, arg3, __int.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_loadf_from_callbacks(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBImage.nstbi_loadf_from_callbacks(long,long,long,long,long,int)"""
        return int.__wrap(__STBImage.nstbi_loadf_from_callbacks(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_info(arg0: 'CharSequence', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImage.stbi_info(java.lang.CharSequence,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool.__wrap(__STBImage.stbi_info(arg0, arg1, arg2, arg3)) 
 
 
# CLASS: org.lwjgl.stb.STBRPContext
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.stb.STBRPContext as __STBRPContext
__STBRPContext = __STBRPContext
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBRPNode as __STBRPNode_Buffer
__Buffer = __STBRPNode_Buffer.Buffer
import org.lwjgl.stb.STBRPNode as __STBRPNode
__STBRPNode = __STBRPNode
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.stb.STBRPContext as __STBRPContext_Buffer
__Buffer = __STBRPContext_Buffer.Buffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBRPContext():
    """org.lwjgl.stb.STBRPContext"""
 
    @staticmethod
    def __wrap(java_value: __STBRPContext) -> 'STBRPContext':
        return STBRPContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBRPContext):
        """
        Dynamic initializer for STBRPContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.create(int)"""
        return Buffer.__wrap(__STBRPContext.create(__int.valueOf(arg0)))

    @overload
    def active_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.active_head()"""
        return 'STBRPNode'.__wrap(super(STBRPContext, self).active_head())

    @staticmethod
    @overload
    def nnum_nodes(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nnum_nodes(long)"""
        return int.__wrap(__STBRPContext.nnum_nodes(__long.valueOf(arg0)))

    @overload
    def width(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.width()"""
        return int.__wrap(super(STBRPContext, self).width())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.createSafe(long)"""
        return STBRPContext.__wrap(__STBRPContext.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.calloc()"""
        return STBRPContext.__wrap(__STBRPContext.calloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.mallocStack(int)"""
        return Buffer.__wrap(__STBRPContext.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nextra(arg0: int, arg1: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.nextra(long,int)"""
        return STBRPNode.__wrap(__STBRPContext.nextra(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nfree_head(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.nfree_head(long)"""
        return STBRPNode.__wrap(__STBRPContext.nfree_head(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.sizeof()"""
        return int.__wrap(super(STBRPContext, self).sizeof())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPContext.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.callocStack()"""
        return STBRPContext.__wrap(__STBRPContext.callocStack())

    @overload
    def free_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.free_head()"""
        return 'STBRPNode'.__wrap(super(STBRPContext, self).free_head())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.calloc(int)"""
        return Buffer.__wrap(__STBRPContext.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.create(long,int)"""
        return Buffer.__wrap(__STBRPContext.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nwidth(long)"""
        return int.__wrap(__STBRPContext.nwidth(__long.valueOf(arg0)))

    @overload
    def num_nodes(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.num_nodes()"""
        return int.__wrap(super(STBRPContext, self).num_nodes())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.malloc(org.lwjgl.system.MemoryStack)"""
        return STBRPContext.__wrap(__STBRPContext.malloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.callocStack(int)"""
        return Buffer.__wrap(__STBRPContext.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.create(long)"""
        return STBRPContext.__wrap(__STBRPContext.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nextra(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPContext.nextra(long)"""
        return Buffer.__wrap(__STBRPContext.nextra(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPContext.__wrap(__STBRPContext.callocStack(arg0))

    @staticmethod
    @overload
    def ninit_mode(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.ninit_mode(long)"""
        return int.__wrap(__STBRPContext.ninit_mode(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def extra(self, arg0: int) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.extra(int)"""
        return 'STBRPNode'.__wrap(super(__STBRPContext, self).extra(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPContext.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.createSafe(long,int)"""
        return Buffer.__wrap(__STBRPContext.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nalign(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nalign(long)"""
        return int.__wrap(__STBRPContext.nalign(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPContext.__wrap(__STBRPContext.mallocStack(arg0))

    @staticmethod
    @overload
    def nheuristic(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nheuristic(long)"""
        return int.__wrap(__STBRPContext.nheuristic(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPContext(java.nio.ByteBuffer)"""
        val = __STBRPContext(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPContext.nheight(long)"""
        return int.__wrap(__STBRPContext.nheight(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.malloc(int)"""
        return Buffer.__wrap(__STBRPContext.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.create()"""
        return STBRPContext.__wrap(__STBRPContext.create())

    @overload
    def height(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.height()"""
        return int.__wrap(super(STBRPContext, self).height())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def mallocStack() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.mallocStack()"""
        return STBRPContext.__wrap(__STBRPContext.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPContext.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def extra(self) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPContext.extra()"""
        return 'Buffer'.__wrap(super(STBRPContext, self).extra())

    @overload
    def init_mode(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.init_mode()"""
        return int.__wrap(super(STBRPContext, self).init_mode())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def heuristic(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.heuristic()"""
        return int.__wrap(super(STBRPContext, self).heuristic())

    @staticmethod
    @overload
    def malloc() -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.malloc()"""
        return STBRPContext.__wrap(__STBRPContext.malloc())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBRPContext':
        """public static org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBRPContext.calloc(org.lwjgl.system.MemoryStack)"""
        return STBRPContext.__wrap(__STBRPContext.calloc(arg0))

    @overload
    def align(self) -> int:
        """public int org.lwjgl.stb.STBRPContext.align()"""
        return int.__wrap(super(STBRPContext, self).align())

    @staticmethod
    @overload
    def nactive_head(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext.nactive_head(long)"""
        return STBRPNode.__wrap(__STBRPContext.nactive_head(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPContext$Buffer org.lwjgl.stb.STBRPContext.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPContext.malloc(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBImageWrite
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.stb.STBImageWrite as __STBImageWrite
__STBImageWrite = __STBImageWrite
from builtins import bool
from builtins import int
 
class STBImageWrite():
    """org.lwjgl.stb.STBImageWrite"""
 
    @staticmethod
    def __wrap(java_value: __STBImageWrite) -> 'STBImageWrite':
        return STBImageWrite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBImageWrite):
        """
        Dynamic initializer for STBImageWrite.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nstbi_write_tga(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_tga(long,int,int,int,long)"""
        return int.__wrap(__STBImageWrite.nstbi_write_tga(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbi_write_hdr_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr_to_func(long,long,int,int,int,long)"""
        return int.__wrap(__STBImageWrite.nstbi_write_hdr_to_func(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.nio.ByteBuffer,int,int,int,java.nio.FloatBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_hdr(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_tga_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_tga_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_tga_to_func(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstbi_write_png_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_png_to_func(long,long,int,int,int,long,int)"""
        return int.__wrap(__STBImageWrite.nstbi_write_png_to_func(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbi_write_jpg(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_jpg(long,int,int,int,long,int)"""
        return int.__wrap(__STBImageWrite.nstbi_write_jpg(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stbi_write_tga(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_tga(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_tga(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_png(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_png(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer,int)"""
        return bool.__wrap(__STBImageWrite.stbi_write_png(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_jpg(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_jpg(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer,int)"""
        return bool.__wrap(__STBImageWrite.stbi_write_jpg(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_write_hdr_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float') -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr_to_func(long,long,int,int,int,float[])"""
        return int.__wrap(__STBImageWrite.nstbi_write_hdr_to_func(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'float') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.nio.ByteBuffer,int,int,int,float[])"""
        return bool.__wrap(__STBImageWrite.stbi_write_hdr(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_hdr_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'FloatBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.FloatBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_hdr_to_func(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstbi_write_bmp(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_bmp(long,int,int,int,long)"""
        return int.__wrap(__STBImageWrite.nstbi_write_bmp(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nstbi_write_bmp_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_bmp_to_func(long,long,int,int,int,long)"""
        return int.__wrap(__STBImageWrite.nstbi_write_bmp_to_func(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_bmp(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_bmp(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_bmp(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'float') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.lang.CharSequence,int,int,int,float[])"""
        return bool.__wrap(__STBImageWrite.stbi_write_hdr(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nstbi_write_hdr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float') -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr(long,int,int,int,float[])"""
        return int.__wrap(__STBImageWrite.nstbi_write_hdr(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stbi_write_jpg_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer', arg6: int) -> int:
        """public static int org.lwjgl.stb.STBImageWrite.stbi_write_jpg_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer,int)"""
        return int.__wrap(__STBImageWrite.stbi_write_jpg_to_func(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __int.valueOf(arg6)))

    @staticmethod
    @overload
    def stbi_write_jpg(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_jpg(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int)"""
        return bool.__wrap(__STBImageWrite.stbi_write_jpg(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_flip_vertically_on_write(arg0: bool):
        """public static void org.lwjgl.stb.STBImageWrite.stbi_flip_vertically_on_write(boolean)"""
        __STBImageWrite.stbi_flip_vertically_on_write(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def stbi_write_hdr(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr(java.lang.CharSequence,int,int,int,java.nio.FloatBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_hdr(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_bmp_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_bmp_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_bmp_to_func(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstbi_write_jpg_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_jpg_to_func(long,long,int,int,int,long,int)"""
        return int.__wrap(__STBImageWrite.nstbi_write_jpg_to_func(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbi_write_tga_to_func(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_tga_to_func(long,long,int,int,int,long)"""
        return int.__wrap(__STBImageWrite.nstbi_write_tga_to_func(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbi_flip_vertically_on_write(arg0: int):
        """public static native void org.lwjgl.stb.STBImageWrite.nstbi_flip_vertically_on_write(int)"""
        __STBImageWrite.nstbi_flip_vertically_on_write(__int.valueOf(arg0))

    @staticmethod
    @overload
    def nstbi_write_hdr(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_hdr(long,int,int,int,long)"""
        return int.__wrap(__STBImageWrite.nstbi_write_hdr(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stbi_write_bmp(arg0: 'CharSequence', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_bmp(java.lang.CharSequence,int,int,int,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_bmp(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def nstbi_write_png(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBImageWrite.nstbi_write_png(long,int,int,int,long,int)"""
        return int.__wrap(__STBImageWrite.nstbi_write_png(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbi_write_tga(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_tga(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBImageWrite.stbi_write_tga(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def stbi_write_hdr_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float') -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_hdr_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,float[])"""
        return bool.__wrap(__STBImageWrite.stbi_write_hdr_to_func(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def stbi_write_png_to_func(arg0: 'STBIWriteCallbackI', arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'ByteBuffer', arg6: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_png_to_func(org.lwjgl.stb.STBIWriteCallbackI,long,int,int,int,java.nio.ByteBuffer,int)"""
        return bool.__wrap(__STBImageWrite.stbi_write_png_to_func(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __int.valueOf(arg6)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def stbi_write_png(arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int, arg4: 'ByteBuffer', arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBImageWrite.stbi_write_png(java.nio.ByteBuffer,int,int,int,java.nio.ByteBuffer,int)"""
        return bool.__wrap(__STBImageWrite.stbi_write_png(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5))) 
 
 
# CLASS: org.lwjgl.stb.STBISkipCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.stb.STBISkipCallback as __STBISkipCallback
__STBISkipCallback = __STBISkipCallback
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
import org.lwjgl.stb.STBISkipCallbackI as __STBISkipCallbackI
__STBISkipCallbackI = __STBISkipCallbackI
from builtins import int
 
class STBISkipCallback(ABC):
    """org.lwjgl.stb.STBISkipCallback"""
 
    @staticmethod
    def __wrap(java_value: __STBISkipCallback) -> 'STBISkipCallback':
        return STBISkipCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBISkipCallback):
        """
        Dynamic initializer for STBISkipCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBISkipCallback.createSafe(long)"""
        return STBISkipCallback.__wrap(__STBISkipCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBISkipCallbackI.callback(long,long)"""
        super(__STBISkipCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.stb.STBISkipCallbackI.invoke(long,int)"""
        pass

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBISkipCallback.create(long)"""
        return STBISkipCallback.__wrap(__STBISkipCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBISkipCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBISkipCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def create(arg0: 'STBISkipCallbackI') -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBISkipCallback.create(org.lwjgl.stb.STBISkipCallbackI)"""
        return STBISkipCallback.__wrap(__STBISkipCallback.create(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBIIOCallbacks$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.stb.STBIReadCallback as __STBIReadCallback
__STBIReadCallback = __STBIReadCallback
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import org.lwjgl.stb.STBIEOFCallback as __STBIEOFCallback
__STBIEOFCallback = __STBIEOFCallback
import java.util.Spliterator as Spliterator
import org.lwjgl.stb.STBISkipCallback as __STBISkipCallback
__STBISkipCallback = __STBISkipCallback
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.stb.STBIIOCallbacks as __STBIIOCallbacks_Buffer
__Buffer = __STBIIOCallbacks_Buffer.Buffer
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBIIOCallbacks.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def eof(self, arg0: 'STBIEOFCallbackI') -> 'Buffer':
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks$Buffer.eof(org.lwjgl.stb.STBIEOFCallbackI)"""
        return 'Buffer'.__wrap(super(__Buffer, self).eof(arg0))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def read(self, arg0: 'STBIReadCallbackI') -> 'Buffer':
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks$Buffer.read(org.lwjgl.stb.STBIReadCallbackI)"""
        return 'Buffer'.__wrap(super(__Buffer, self).read(arg0))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def eof(self) -> 'STBIEOFCallback':
        """public org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIIOCallbacks$Buffer.eof()"""
        return 'STBIEOFCallback'.__wrap(super(Buffer, self).eof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def read(self) -> 'STBIReadCallback':
        """public org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIIOCallbacks$Buffer.read()"""
        return 'STBIReadCallback'.__wrap(super(Buffer, self).read())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def skip(self, arg0: 'STBISkipCallbackI') -> 'Buffer':
        """public org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks$Buffer.skip(org.lwjgl.stb.STBISkipCallbackI)"""
        return 'Buffer'.__wrap(super(__Buffer, self).skip(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def skip(self) -> 'STBISkipCallback':
        """public org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBIIOCallbacks$Buffer.skip()"""
        return 'STBISkipCallback'.__wrap(super(Buffer, self).skip())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBTTVertex$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import org.lwjgl.stb.STBTTVertex as __STBTTVertex_Buffer
__Buffer = __STBTTVertex_Buffer.Buffer
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTVertex.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def cy1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cy1()"""
        return int.__wrap(super(Buffer, self).cy1())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def type(self) -> int:
        """public byte org.lwjgl.stb.STBTTVertex$Buffer.type()"""
        return int.__wrap(super(Buffer, self).type())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def cx1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cx1()"""
        return int.__wrap(super(Buffer, self).cx1())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTVertex$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def cy(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cy()"""
        return int.__wrap(super(Buffer, self).cy())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def y(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.y()"""
        return int.__wrap(super(Buffer, self).y())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def cx(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.cx()"""
        return int.__wrap(super(Buffer, self).cx())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def x(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex$Buffer.x()"""
        return int.__wrap(super(Buffer, self).x())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTVertex$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBIWriteCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.stb.STBIWriteCallback as __STBIWriteCallback
__STBIWriteCallback = __STBIWriteCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.lwjgl.stb.STBIWriteCallbackI as __STBIWriteCallbackI
__STBIWriteCallbackI = __STBIWriteCallbackI
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBIWriteCallback(ABC):
    """org.lwjgl.stb.STBIWriteCallback"""
 
    @staticmethod
    def __wrap(java_value: __STBIWriteCallback) -> 'STBIWriteCallback':
        return STBIWriteCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIWriteCallback):
        """
        Dynamic initializer for STBIWriteCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIWriteCallbackI.callback(long,long)"""
        super(__STBIWriteCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIWriteCallback':
        """public static org.lwjgl.stb.STBIWriteCallback org.lwjgl.stb.STBIWriteCallback.create(long)"""
        return STBIWriteCallback.__wrap(__STBIWriteCallback.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIWriteCallback':
        """public static org.lwjgl.stb.STBIWriteCallback org.lwjgl.stb.STBIWriteCallback.createSafe(long)"""
        return STBIWriteCallback.__wrap(__STBIWriteCallback.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: 'STBIWriteCallbackI') -> 'STBIWriteCallback':
        """public static org.lwjgl.stb.STBIWriteCallback org.lwjgl.stb.STBIWriteCallback.create(org.lwjgl.stb.STBIWriteCallbackI)"""
        return STBIWriteCallback.__wrap(__STBIWriteCallback.create(arg0))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getData(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBIWriteCallback.getData(long,int)"""
        return ByteBuffer.__wrap(__STBIWriteCallback.getData(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.stb.STBIWriteCallbackI.invoke(long,long,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIWriteCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIWriteCallbackI, self).getCallInterface())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisComment
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBVorbisComment as __STBVorbisComment
__STBVorbisComment = __STBVorbisComment
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.stb.STBVorbisComment as __STBVorbisComment_Buffer
__Buffer = __STBVorbisComment_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import int
 
class STBVorbisComment():
    """org.lwjgl.stb.STBVorbisComment"""
 
    @staticmethod
    def __wrap(java_value: __STBVorbisComment) -> 'STBVorbisComment':
        return STBVorbisComment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBVorbisComment):
        """
        Dynamic initializer for STBVorbisComment.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ncomment_list(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.stb.STBVorbisComment.ncomment_list(long)"""
        return pygl.PointerBuffer.__wrap(__STBVorbisComment.ncomment_list(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nvendor(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBVorbisComment.nvendor(long)"""
        return ByteBuffer.__wrap(__STBVorbisComment.nvendor(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.malloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisComment.__wrap(__STBVorbisComment.malloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.createSafe(long,int)"""
        return Buffer.__wrap(__STBVorbisComment.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def vendorString(self) -> str:
        """public java.lang.String org.lwjgl.stb.STBVorbisComment.vendorString()"""
        return str.__wrap(super(STBVorbisComment, self).vendorString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.create(long)"""
        return STBVorbisComment.__wrap(__STBVorbisComment.create(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisComment(java.nio.ByteBuffer)"""
        val = __STBVorbisComment(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def vendor(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisComment.vendor()"""
        return 'ByteBuffer'.__wrap(super(STBVorbisComment, self).vendor())

    @staticmethod
    @overload
    def create() -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.create()"""
        return STBVorbisComment.__wrap(__STBVorbisComment.create())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.create(long,int)"""
        return Buffer.__wrap(__STBVorbisComment.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisComment.calloc(__int.valueOf(arg0), arg1))

    @overload
    def comment_list(self) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.stb.STBVorbisComment.comment_list()"""
        return 'pygl.PointerBuffer'.__wrap(super(STBVorbisComment, self).comment_list())

    @staticmethod
    @overload
    def ncomment_list_length(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisComment.ncomment_list_length(long)"""
        return int.__wrap(__STBVorbisComment.ncomment_list_length(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.calloc()"""
        return STBVorbisComment.__wrap(__STBVorbisComment.calloc())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.calloc(int)"""
        return Buffer.__wrap(__STBVorbisComment.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def malloc() -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.malloc()"""
        return STBVorbisComment.__wrap(__STBVorbisComment.malloc())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.create(int)"""
        return Buffer.__wrap(__STBVorbisComment.create(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBVorbisComment.sizeof()"""
        return int.__wrap(super(STBVorbisComment, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.calloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisComment.__wrap(__STBVorbisComment.calloc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def comment_list_length(self) -> int:
        """public int org.lwjgl.stb.STBVorbisComment.comment_list_length()"""
        return int.__wrap(super(STBVorbisComment, self).comment_list_length())

    @staticmethod
    @overload
    def nvendorString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.stb.STBVorbisComment.nvendorString(long)"""
        return str.__wrap(__STBVorbisComment.nvendorString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.malloc(int)"""
        return Buffer.__wrap(__STBVorbisComment.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisComment$Buffer org.lwjgl.stb.STBVorbisComment.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisComment.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBVorbisComment':
        """public static org.lwjgl.stb.STBVorbisComment org.lwjgl.stb.STBVorbisComment.createSafe(long)"""
        return STBVorbisComment.__wrap(__STBVorbisComment.createSafe(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackRange
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBTTPackRange as __STBTTPackRange
__STBTTPackRange = __STBTTPackRange
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import org.lwjgl.stb.STBTTPackedchar as __STBTTPackedchar_Buffer
__Buffer = __STBTTPackedchar_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.stb.STBTTPackRange as __STBTTPackRange_Buffer
__Buffer = __STBTTPackRange_Buffer.Buffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTPackRange():
    """org.lwjgl.stb.STBTTPackRange"""
 
    @staticmethod
    def __wrap(java_value: __STBTTPackRange) -> 'STBTTPackRange':
        return STBTTPackRange(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTPackRange):
        """
        Dynamic initializer for STBTTPackRange.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.createSafe(long)"""
        return STBTTPackRange.__wrap(__STBTTPackRange.createSafe(__long.valueOf(arg0)))

    @overload
    def num_chars(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.num_chars(int)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).num_chars(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBTTPackRange.validate(long)"""
        __STBTTPackRange.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange.__wrap(__STBTTPackRange.mallocStack(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.mallocStack()"""
        return STBTTPackRange.__wrap(__STBTTPackRange.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange.__wrap(__STBTTPackRange.callocStack(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def font_size(self, arg0: float) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.font_size(float)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).font_size(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def nv_oversample(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nv_oversample(long,byte)"""
        __STBTTPackRange.nv_oversample(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def nnum_chars(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nnum_chars(long,int)"""
        __STBTTPackRange.nnum_chars(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.calloc(int)"""
        return Buffer.__wrap(__STBTTPackRange.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackRange.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nfont_size(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackRange.nfont_size(long)"""
        return float.__wrap(__STBTTPackRange.nfont_size(__long.valueOf(arg0)))

    @overload
    def chardata_for_range(self, arg0: 'Buffer') -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.chardata_for_range(org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).chardata_for_range(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackRange.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange.sizeof()"""
        return int.__wrap(super(STBTTPackRange, self).sizeof())

    @staticmethod
    @overload
    def nnum_chars(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackRange.nnum_chars(long)"""
        return int.__wrap(__STBTTPackRange.nnum_chars(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.malloc()"""
        return STBTTPackRange.__wrap(__STBTTPackRange.malloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.mallocStack(int)"""
        return Buffer.__wrap(__STBTTPackRange.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nh_oversample(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nh_oversample(long,byte)"""
        __STBTTPackRange.nh_oversample(__long.valueOf(arg0), __byte.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def h_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange.h_oversample()"""
        return int.__wrap(super(STBTTPackRange, self).h_oversample())

    @overload
    def array_of_unicode_codepoints(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.stb.STBTTPackRange.array_of_unicode_codepoints()"""
        return 'IntBuffer'.__wrap(super(STBTTPackRange, self).array_of_unicode_codepoints())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def num_chars(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange.num_chars()"""
        return int.__wrap(super(STBTTPackRange, self).num_chars())

    @staticmethod
    @overload
    def nfont_size(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackRange.nfont_size(long,float)"""
        __STBTTPackRange.nfont_size(__long.valueOf(arg0), __float.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange.__wrap(__STBTTPackRange.calloc(arg0))

    @staticmethod
    @overload
    def narray_of_unicode_codepoints(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.stb.STBTTPackRange.narray_of_unicode_codepoints(long)"""
        return IntBuffer.__wrap(__STBTTPackRange.narray_of_unicode_codepoints(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.callocStack()"""
        return STBTTPackRange.__wrap(__STBTTPackRange.callocStack())

    @staticmethod
    @overload
    def narray_of_unicode_codepoints(arg0: int, arg1: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTTPackRange.narray_of_unicode_codepoints(long,java.nio.IntBuffer)"""
        __STBTTPackRange.narray_of_unicode_codepoints(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nchardata_for_range(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackRange.nchardata_for_range(long)"""
        return Buffer.__wrap(__STBTTPackRange.nchardata_for_range(__long.valueOf(arg0)))

    @overload
    def first_unicode_codepoint_in_range(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.first_unicode_codepoint_in_range(int)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).first_unicode_codepoint_in_range(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: 'STBTTPackRange') -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.set(org.lwjgl.stb.STBTTPackRange)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).set(arg0))

    @staticmethod
    @overload
    def nh_oversample(arg0: int) -> int:
        """public static byte org.lwjgl.stb.STBTTPackRange.nh_oversample(long)"""
        return int.__wrap(__STBTTPackRange.nh_oversample(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.calloc()"""
        return STBTTPackRange.__wrap(__STBTTPackRange.calloc())

    @staticmethod
    @overload
    def nfirst_unicode_codepoint_in_range(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTPackRange.nfirst_unicode_codepoint_in_range(long)"""
        return int.__wrap(__STBTTPackRange.nfirst_unicode_codepoint_in_range(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nfirst_unicode_codepoint_in_range(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackRange.nfirst_unicode_codepoint_in_range(long,int)"""
        __STBTTPackRange.nfirst_unicode_codepoint_in_range(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def array_of_unicode_codepoints(self, arg0: 'IntBuffer') -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.array_of_unicode_codepoints(java.nio.IntBuffer)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).array_of_unicode_codepoints(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.create(int)"""
        return Buffer.__wrap(__STBTTPackRange.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackRange.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def v_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange.v_oversample()"""
        return int.__wrap(super(STBTTPackRange, self).v_oversample())

    @overload
    def h_oversample(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.h_oversample(byte)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).h_oversample(__byte.valueOf(arg0)))

    @overload
    def v_oversample(self, arg0: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.v_oversample(byte)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).v_oversample(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.create()"""
        return STBTTPackRange.__wrap(__STBTTPackRange.create())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.malloc(int)"""
        return Buffer.__wrap(__STBTTPackRange.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nv_oversample(arg0: int) -> int:
        """public static byte org.lwjgl.stb.STBTTPackRange.nv_oversample(long)"""
        return int.__wrap(__STBTTPackRange.nv_oversample(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def font_size(self) -> float:
        """public float org.lwjgl.stb.STBTTPackRange.font_size()"""
        return float.__wrap(super(STBTTPackRange, self).font_size())

    @overload
    def set(self, arg0: float, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'Buffer', arg5: int, arg6: int) -> 'STBTTPackRange':
        """public org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.set(float,int,java.nio.IntBuffer,int,org.lwjgl.stb.STBTTPackedchar$Buffer,byte,byte)"""
        return 'STBTTPackRange'.__wrap(super(__STBTTPackRange, self).set(__float.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __byte.valueOf(arg5), __byte.valueOf(arg6)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTPackRange.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def chardata_for_range(self) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackRange.chardata_for_range()"""
        return 'Buffer'.__wrap(super(STBTTPackRange, self).chardata_for_range())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackRange.__wrap(__STBTTPackRange.malloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackRange.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTPackRange':
        """public static org.lwjgl.stb.STBTTPackRange org.lwjgl.stb.STBTTPackRange.create(long)"""
        return STBTTPackRange.__wrap(__STBTTPackRange.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nchardata_for_range(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.stb.STBTTPackRange.nchardata_for_range(long,org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        __STBTTPackRange.nchardata_for_range(__long.valueOf(arg0), arg1)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def first_unicode_codepoint_in_range(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange.first_unicode_codepoint_in_range()"""
        return int.__wrap(super(STBTTPackRange, self).first_unicode_codepoint_in_range())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.callocStack(int)"""
        return Buffer.__wrap(__STBTTPackRange.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange.create(long,int)"""
        return Buffer.__wrap(__STBTTPackRange.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackRange(java.nio.ByteBuffer)"""
        val = __STBTTPackRange(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.lwjgl.stb.STBTTPackRange$Buffer
from pyquantum_helper import import_once as __import_once__
import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import float
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.Float as __float
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.stb.STBTTPackedchar as __STBTTPackedchar_Buffer
__Buffer = __STBTTPackedchar_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.stb.STBTTPackRange as __STBTTPackRange_Buffer
__Buffer = __STBTTPackRange_Buffer.Buffer
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTPackRange.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def font_size(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.font_size(float)"""
        return 'Buffer'.__wrap(super(__Buffer, self).font_size(__float.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def font_size(self) -> float:
        """public float org.lwjgl.stb.STBTTPackRange$Buffer.font_size()"""
        return float.__wrap(super(Buffer, self).font_size())

    @overload
    def num_chars(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange$Buffer.num_chars()"""
        return int.__wrap(super(Buffer, self).num_chars())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def v_oversample(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.v_oversample(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).v_oversample(__byte.valueOf(arg0)))

    @overload
    def first_unicode_codepoint_in_range(self) -> int:
        """public int org.lwjgl.stb.STBTTPackRange$Buffer.first_unicode_codepoint_in_range()"""
        return int.__wrap(super(Buffer, self).first_unicode_codepoint_in_range())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def v_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange$Buffer.v_oversample()"""
        return int.__wrap(super(Buffer, self).v_oversample())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackRange$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def first_unicode_codepoint_in_range(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.first_unicode_codepoint_in_range(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).first_unicode_codepoint_in_range(__int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def h_oversample(self) -> int:
        """public byte org.lwjgl.stb.STBTTPackRange$Buffer.h_oversample()"""
        return int.__wrap(super(Buffer, self).h_oversample())

    @overload
    def num_chars(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.num_chars(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).num_chars(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTPackRange$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def array_of_unicode_codepoints(self, arg0: 'IntBuffer') -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.array_of_unicode_codepoints(java.nio.IntBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).array_of_unicode_codepoints(arg0))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def h_oversample(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.h_oversample(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).h_oversample(__byte.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def chardata_for_range(self) -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.chardata_for_range()"""
        return 'Buffer'.__wrap(super(Buffer, self).chardata_for_range())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def array_of_unicode_codepoints(self) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.stb.STBTTPackRange$Buffer.array_of_unicode_codepoints()"""
        return 'IntBuffer'.__wrap(super(Buffer, self).array_of_unicode_codepoints())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def chardata_for_range(self, arg0: 'Buffer') -> 'Buffer':
        """public org.lwjgl.stb.STBTTPackRange$Buffer org.lwjgl.stb.STBTTPackRange$Buffer.chardata_for_range(org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).chardata_for_range(arg0))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBTTKerningentry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBTTKerningentry as __STBTTKerningentry_Buffer
__Buffer = __STBTTKerningentry_Buffer.Buffer
import org.lwjgl.stb.STBTTKerningentry as __STBTTKerningentry
__STBTTKerningentry = __STBTTKerningentry
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTKerningentry():
    """org.lwjgl.stb.STBTTKerningentry"""
 
    @staticmethod
    def __wrap(java_value: __STBTTKerningentry) -> 'STBTTKerningentry':
        return STBTTKerningentry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTKerningentry):
        """
        Dynamic initializer for STBTTKerningentry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.malloc(int)"""
        return Buffer.__wrap(__STBTTKerningentry.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTKerningentry.__wrap(__STBTTKerningentry.calloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.create()"""
        return STBTTKerningentry.__wrap(__STBTTKerningentry.create())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.sizeof()"""
        return int.__wrap(super(STBTTKerningentry, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.createSafe(long)"""
        return STBTTKerningentry.__wrap(__STBTTKerningentry.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglyph2(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTKerningentry.nglyph2(long)"""
        return int.__wrap(__STBTTKerningentry.nglyph2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nadvance(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTKerningentry.nadvance(long)"""
        return int.__wrap(__STBTTKerningentry.nadvance(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def glyph2(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.glyph2()"""
        return int.__wrap(super(STBTTKerningentry, self).glyph2())

    @staticmethod
    @overload
    def calloc() -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.calloc()"""
        return STBTTKerningentry.__wrap(__STBTTKerningentry.calloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.create(long,int)"""
        return Buffer.__wrap(__STBTTKerningentry.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def advance(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.advance()"""
        return int.__wrap(super(STBTTKerningentry, self).advance())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTKerningentry.__wrap(__STBTTKerningentry.malloc(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTKerningentry(java.nio.ByteBuffer)"""
        val = __STBTTKerningentry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def glyph1(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry.glyph1()"""
        return int.__wrap(super(STBTTKerningentry, self).glyph1())

    @staticmethod
    @overload
    def malloc() -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.malloc()"""
        return STBTTKerningentry.__wrap(__STBTTKerningentry.malloc())

    @staticmethod
    @overload
    def nglyph1(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTKerningentry.nglyph1(long)"""
        return int.__wrap(__STBTTKerningentry.nglyph1(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.calloc(int)"""
        return Buffer.__wrap(__STBTTKerningentry.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTKerningentry':
        """public static org.lwjgl.stb.STBTTKerningentry org.lwjgl.stb.STBTTKerningentry.create(long)"""
        return STBTTKerningentry.__wrap(__STBTTKerningentry.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.create(int)"""
        return Buffer.__wrap(__STBTTKerningentry.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTKerningentry.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTKerningentry.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTKerningentry$Buffer org.lwjgl.stb.STBTTKerningentry.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTKerningentry.malloc(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackContext$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.stb.STBRPContext as __STBRPContext
__STBRPContext = __STBRPContext
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBRPNode as __STBRPNode_Buffer
__Buffer = __STBRPNode_Buffer.Buffer
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.stb.STBTTPackContext as __STBTTPackContext_Buffer
__Buffer = __STBTTPackContext_Buffer.Buffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTPackContext.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def stride_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.stride_in_bytes()"""
        return int.__wrap(super(Buffer, self).stride_in_bytes())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def user_allocator_context(self) -> int:
        """public long org.lwjgl.stb.STBTTPackContext$Buffer.user_allocator_context()"""
        return int.__wrap(super(Buffer, self).user_allocator_context())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTPackContext$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def v_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.v_oversample()"""
        return int.__wrap(super(Buffer, self).v_oversample())

    @overload
    def height(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.height()"""
        return int.__wrap(super(Buffer, self).height())

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def nodes(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBTTPackContext$Buffer.nodes(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).nodes(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTPackContext$Buffer.pixels(int)"""
        return 'ByteBuffer'.__wrap(super(__Buffer, self).pixels(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def skip_missing(self) -> bool:
        """public boolean org.lwjgl.stb.STBTTPackContext$Buffer.skip_missing()"""
        return bool.__wrap(super(Buffer, self).skip_missing())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def width(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.width()"""
        return int.__wrap(super(Buffer, self).width())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def h_oversample(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.h_oversample()"""
        return int.__wrap(super(Buffer, self).h_oversample())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackContext$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def pack_info(self) -> 'STBRPContext':
        """public org.lwjgl.stb.STBRPContext org.lwjgl.stb.STBTTPackContext$Buffer.pack_info()"""
        return 'STBRPContext'.__wrap(super(Buffer, self).pack_info())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def padding(self) -> int:
        """public int org.lwjgl.stb.STBTTPackContext$Buffer.padding()"""
        return int.__wrap(super(Buffer, self).padding())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBIIOCallbacks
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.stb.STBIReadCallback as __STBIReadCallback
__STBIReadCallback = __STBIReadCallback
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBIIOCallbacks as __STBIIOCallbacks
__STBIIOCallbacks = __STBIIOCallbacks
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import org.lwjgl.stb.STBIEOFCallback as __STBIEOFCallback
__STBIEOFCallback = __STBIEOFCallback
import org.lwjgl.stb.STBISkipCallback as __STBISkipCallback
__STBISkipCallback = __STBISkipCallback
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import org.lwjgl.stb.STBIIOCallbacks as __STBIIOCallbacks_Buffer
__Buffer = __STBIIOCallbacks_Buffer.Buffer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBIIOCallbacks():
    """org.lwjgl.stb.STBIIOCallbacks"""
 
    @staticmethod
    def __wrap(java_value: __STBIIOCallbacks) -> 'STBIIOCallbacks':
        return STBIIOCallbacks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIIOCallbacks):
        """
        Dynamic initializer for STBIIOCallbacks.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.malloc(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.malloc(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBIIOCallbacks.validate(long)"""
        __STBIIOCallbacks.validate(__long.valueOf(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def read(self, arg0: 'STBIReadCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.read(org.lwjgl.stb.STBIReadCallbackI)"""
        return 'STBIIOCallbacks'.__wrap(super(__STBIIOCallbacks, self).read(arg0))

    @staticmethod
    @overload
    def nskip(arg0: int) -> 'STBISkipCallback':
        """public static org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBIIOCallbacks.nskip(long)"""
        return STBISkipCallback.__wrap(__STBIIOCallbacks.nskip(__long.valueOf(arg0)))

    @overload
    def eof(self) -> 'STBIEOFCallback':
        """public org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIIOCallbacks.eof()"""
        return 'STBIEOFCallback'.__wrap(super(STBIIOCallbacks, self).eof())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.create(long)"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBIIOCallbacks.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nskip(arg0: int, arg1: 'STBISkipCallbackI'):
        """public static void org.lwjgl.stb.STBIIOCallbacks.nskip(long,org.lwjgl.stb.STBISkipCallbackI)"""
        __STBIIOCallbacks.nskip(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.callocStack(int)"""
        return Buffer.__wrap(__STBIIOCallbacks.callocStack(__int.valueOf(arg0)))

    @overload
    def read(self) -> 'STBIReadCallback':
        """public org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIIOCallbacks.read()"""
        return 'STBIReadCallback'.__wrap(super(STBIIOCallbacks, self).read())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.create(long,int)"""
        return Buffer.__wrap(__STBIIOCallbacks.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.calloc(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.calloc(arg0))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def neof(arg0: int, arg1: 'STBIEOFCallbackI'):
        """public static void org.lwjgl.stb.STBIIOCallbacks.neof(long,org.lwjgl.stb.STBIEOFCallbackI)"""
        __STBIIOCallbacks.neof(__long.valueOf(arg0), arg1)

    @overload
    def skip(self) -> 'STBISkipCallback':
        """public org.lwjgl.stb.STBISkipCallback org.lwjgl.stb.STBIIOCallbacks.skip()"""
        return 'STBISkipCallback'.__wrap(super(STBIIOCallbacks, self).skip())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.mallocStack(int)"""
        return Buffer.__wrap(__STBIIOCallbacks.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.createSafe(long)"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBIIOCallbacks.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.create()"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.create())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.callocStack(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.mallocStack(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.create(int)"""
        return Buffer.__wrap(__STBIIOCallbacks.create(__int.valueOf(arg0)))

    @overload
    def eof(self, arg0: 'STBIEOFCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.eof(org.lwjgl.stb.STBIEOFCallbackI)"""
        return 'STBIIOCallbacks'.__wrap(super(__STBIIOCallbacks, self).eof(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBIIOCallbacks.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'STBIReadCallbackI', arg1: 'STBISkipCallbackI', arg2: 'STBIEOFCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.set(org.lwjgl.stb.STBIReadCallbackI,org.lwjgl.stb.STBISkipCallbackI,org.lwjgl.stb.STBIEOFCallbackI)"""
        return 'STBIIOCallbacks'.__wrap(super(__STBIIOCallbacks, self).set(arg0, arg1, arg2))

    @staticmethod
    @overload
    def nread(arg0: int, arg1: 'STBIReadCallbackI'):
        """public static void org.lwjgl.stb.STBIIOCallbacks.nread(long,org.lwjgl.stb.STBIReadCallbackI)"""
        __STBIIOCallbacks.nread(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.malloc(int)"""
        return Buffer.__wrap(__STBIIOCallbacks.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.calloc(int)"""
        return Buffer.__wrap(__STBIIOCallbacks.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBIIOCallbacks.sizeof()"""
        return int.__wrap(super(STBIIOCallbacks, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.createSafe(long,int)"""
        return Buffer.__wrap(__STBIIOCallbacks.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBIIOCallbacks$Buffer org.lwjgl.stb.STBIIOCallbacks.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBIIOCallbacks.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.malloc()"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.malloc())

    @staticmethod
    @overload
    def calloc() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.calloc()"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.calloc())

    @staticmethod
    @overload
    def callocStack() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.callocStack()"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.callocStack())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'STBIIOCallbacks':
        """public static org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.mallocStack()"""
        return STBIIOCallbacks.__wrap(__STBIIOCallbacks.mallocStack())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'STBIIOCallbacks') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.set(org.lwjgl.stb.STBIIOCallbacks)"""
        return 'STBIIOCallbacks'.__wrap(super(__STBIIOCallbacks, self).set(arg0))

    @overload
    def skip(self, arg0: 'STBISkipCallbackI') -> 'STBIIOCallbacks':
        """public org.lwjgl.stb.STBIIOCallbacks org.lwjgl.stb.STBIIOCallbacks.skip(org.lwjgl.stb.STBISkipCallbackI)"""
        return 'STBIIOCallbacks'.__wrap(super(__STBIIOCallbacks, self).skip(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nread(arg0: int) -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIIOCallbacks.nread(long)"""
        return STBIReadCallback.__wrap(__STBIIOCallbacks.nread(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def neof(arg0: int) -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIIOCallbacks.neof(long)"""
        return STBIEOFCallback.__wrap(__STBIIOCallbacks.neof(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBIIOCallbacks(java.nio.ByteBuffer)"""
        val = __STBIIOCallbacks(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.lwjgl.stb.STBTruetype
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
from builtins import float
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.stb.STBTruetype as __STBTruetype
__STBTruetype = __STBTruetype
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.stb.STBTTVertex as __STBTTVertex_Buffer
__Buffer = __STBTTVertex_Buffer.Buffer
from builtins import bool
from builtins import int
 
class STBTruetype():
    """org.lwjgl.stb.STBTruetype"""
 
    @staticmethod
    def __wrap(java_value: __STBTruetype) -> 'STBTruetype':
        return STBTruetype(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTruetype):
        """
        Dynamic initializer for STBTruetype.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def stbtt_FindGlyphIndex(arg0: 'STBTTFontinfo', arg1: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_FindGlyphIndex(org.lwjgl.stb.STBTTFontinfo,int)"""
        return int.__wrap(__STBTruetype.stbtt_FindGlyphIndex(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,int[],int[],int[],int[])"""
        __STBTruetype.stbtt_GetCodepointBitmapBox(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def STBTT_POINT_SIZE(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.STBTT_POINT_SIZE(int)"""
        return int.__wrap(__STBTruetype.STBTT_POINT_SIZE(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nstbtt_GetPackedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetPackedQuad(long,int,int,int,float[],float[],long,int)"""
        __STBTruetype.nstbtt_GetPackedQuad(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_GetNumberOfFonts(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetNumberOfFonts(long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetNumberOfFonts(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stbtt_GetNumberOfFonts(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetNumberOfFonts(java.nio.ByteBuffer)"""
        return int.__wrap(__STBTruetype.stbtt_GetNumberOfFonts(arg0))

    @staticmethod
    @overload
    def nstbtt_GetFontBoundingBox(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontBoundingBox(long,int[],int[],int[],int[])"""
        __STBTruetype.nstbtt_GetFontBoundingBox(__long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def stbtt_FindSVGDoc(arg0: 'STBTTFontinfo', arg1: int) -> int:
        """public static long org.lwjgl.stb.STBTruetype.stbtt_FindSVGDoc(org.lwjgl.stb.STBTTFontinfo,int)"""
        return int.__wrap(__STBTruetype.stbtt_FindSVGDoc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetGlyphBitmapBox(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def nstbtt_PackSetSkipMissingCodepoints(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackSetSkipMissingCodepoints(long,int)"""
        __STBTruetype.nstbtt_PackSetSkipMissingCodepoints(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_FindGlyphIndex(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_FindGlyphIndex(long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_FindGlyphIndex(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_PackFontRanges(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: 'Buffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackFontRanges(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,org.lwjgl.stb.STBTTPackRange$Buffer)"""
        return bool.__wrap(__STBTruetype.stbtt_PackFontRanges(arg0, arg1, __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def stbtt_GetCodepointHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointHMetrics(org.lwjgl.stb.STBTTFontinfo,int,int[],int[])"""
        __STBTruetype.stbtt_GetCodepointHMetrics(arg0, __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nstbtt_PackBegin(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackBegin(long,long,int,int,int,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_PackBegin(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointShape(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointShape(long,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointShape(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapSubpixel(long,float,float,float,float,int,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointBitmapSubpixel(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_CompareUTF8toUTF16_bigendian(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_CompareUTF8toUTF16_bigendian(long,int,long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_CompareUTF8toUTF16_bigendian(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stbtt_GetCodepointHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointHMetrics(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetCodepointHMetrics(arg0, __int.valueOf(arg1), arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def stbtt_FindMatchingFont(arg0: 'ByteBuffer', arg1: 'CharSequence', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_FindMatchingFont(java.nio.ByteBuffer,java.lang.CharSequence,int)"""
        return int.__wrap(__STBTruetype.stbtt_FindMatchingFont(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetGlyphSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetGlyphSDF(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_ScaleForPixelHeight(arg0: int, arg1: float) -> float:
        """public static native float org.lwjgl.stb.STBTruetype.nstbtt_ScaleForPixelHeight(long,float)"""
        return float.__wrap(__STBTruetype.nstbtt_ScaleForPixelHeight(__long.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetFontVMetrics(arg0: 'STBTTFontinfo', arg1: 'int', arg2: 'int', arg3: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetrics(org.lwjgl.stb.STBTTFontinfo,int[],int[],int[])"""
        __STBTruetype.stbtt_GetFontVMetrics(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        __STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, arg12, __int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_PackSetOversampling(arg0: 'STBTTPackContext', arg1: int, arg2: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackSetOversampling(org.lwjgl.stb.STBTTPackContext,int,int)"""
        __STBTruetype.stbtt_PackSetOversampling(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(long,int,float,float,float,float,int[],int[],int[],int[])"""
        __STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def stbtt_FreeSDF(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeSDF(java.nio.ByteBuffer,long)"""
        __STBTruetype.stbtt_FreeSDF(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def stbtt_PackFontRangesGatherRects(arg0: 'STBTTPackContext', arg1: 'STBTTFontinfo', arg2: 'Buffer', arg3: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_PackFontRangesGatherRects(org.lwjgl.stb.STBTTPackContext,org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTPackRange$Buffer,org.lwjgl.stb.STBRPRect$Buffer)"""
        return int.__wrap(__STBTruetype.stbtt_PackFontRangesGatherRects(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(long,int,float,float,float,float,int[],int[],int[],int[])"""
        __STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def stbtt_FreeSDF(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeSDF(java.nio.ByteBuffer)"""
        __STBTruetype.stbtt_FreeSDF(arg0)

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,int[],int[],int[],int[])"""
        __STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def nstbtt_GetFontVMetricsOS2(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int') -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetricsOS2(long,int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetFontVMetricsOS2(__long.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapSubpixel(long,float,float,float,float,int,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphBitmapSubpixel(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphShape(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphShape(long,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphShape(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_FreeShape(arg0: 'STBTTFontinfo', arg1: 'Buffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeShape(org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTVertex$Buffer)"""
        __STBTruetype.stbtt_FreeShape(arg0, arg1)

    @staticmethod
    @overload
    def stbtt_GetPackedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetPackedQuad(org.lwjgl.stb.STBTTPackedchar$Buffer,int,int,int,float[],float[],org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        __STBTruetype.stbtt_GetPackedQuad(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, __boolean.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'FloatBuffer', arg12: 'FloatBuffer', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,int)"""
        __STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, arg12, __int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_GetGlyphSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,int[],int[],int[],int[])"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetGlyphSDF(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetFontNameString(arg0: 'STBTTFontinfo', arg1: int, arg2: int, arg3: int, arg4: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetFontNameString(org.lwjgl.stb.STBTTFontinfo,int,int,int,int)"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetFontNameString(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbtt_PackFontRangesPackRects(arg0: 'STBTTPackContext', arg1: 'Buffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackFontRangesPackRects(org.lwjgl.stb.STBTTPackContext,org.lwjgl.stb.STBRPRect$Buffer)"""
        __STBTruetype.stbtt_PackFontRangesPackRects(arg0, arg1)

    @staticmethod
    @overload
    def stbtt_GetGlyphShape(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetGlyphShape(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBTruetype.stbtt_GetGlyphShape(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstbtt_PackFontRangesGatherRects(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRangesGatherRects(long,long,long,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_PackFontRangesGatherRects(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int)"""
        __STBTruetype.stbtt_MakeGlyphBitmapSubpixel(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nstbtt_GetScaledFontVMetrics(arg0: int, arg1: int, arg2: float, arg3: 'float', arg4: 'float', arg5: 'float'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetScaledFontVMetrics(long,int,float,float[],float[],float[])"""
        __STBTruetype.nstbtt_GetScaledFontVMetrics(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), arg3, arg4, arg5)

    @staticmethod
    @overload
    def nstbtt_GetFontVMetrics(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetrics(long,int[],int[],int[])"""
        __STBTruetype.nstbtt_GetFontVMetrics(__long.valueOf(arg0), arg1, arg2, arg3)

    @staticmethod
    @overload
    def stbtt_PackEnd(arg0: 'STBTTPackContext'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackEnd(org.lwjgl.stb.STBTTPackContext)"""
        __STBTruetype.stbtt_PackEnd(arg0)

    @staticmethod
    @overload
    def nstbtt_IsGlyphEmpty(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_IsGlyphEmpty(long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_IsGlyphEmpty(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def stbtt_GetFontVMetrics(arg0: 'STBTTFontinfo', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetrics(org.lwjgl.stb.STBTTFontinfo,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetFontVMetrics(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def nstbtt_GetFontVMetrics(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetrics(long,long,long,long)"""
        __STBTruetype.nstbtt_GetFontVMetrics(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nstbtt_FreeBitmap(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_FreeBitmap(long,long)"""
        __STBTruetype.nstbtt_FreeBitmap(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmap(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmap(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,int)"""
        __STBTruetype.stbtt_MakeCodepointBitmap(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_BakeFontBitmap(arg0: 'ByteBuffer', arg1: float, arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int, arg6: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_BakeFontBitmap(java.nio.ByteBuffer,float,java.nio.ByteBuffer,int,int,int,org.lwjgl.stb.STBTTBakedChar$Buffer)"""
        return int.__wrap(__STBTruetype.stbtt_BakeFontBitmap(arg0, __float.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmap(long,float,float,int,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphBitmap(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        __STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, arg12, __int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmap(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmap(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,int)"""
        __STBTruetype.stbtt_MakeGlyphBitmap(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,long,long,int)"""
        __STBTruetype.nstbtt_MakeCodepointBitmapSubpixelPrefilter(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12), __int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_ScaleForMappingEmToPixels(arg0: 'STBTTFontinfo', arg1: float) -> float:
        """public static float org.lwjgl.stb.STBTruetype.stbtt_ScaleForMappingEmToPixels(org.lwjgl.stb.STBTTFontinfo,float)"""
        return float.__wrap(__STBTruetype.stbtt_ScaleForMappingEmToPixels(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetFontBoundingBox(arg0: 'STBTTFontinfo', arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontBoundingBox(org.lwjgl.stb.STBTTFontinfo,int[],int[],int[],int[])"""
        __STBTruetype.stbtt_GetFontBoundingBox(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def stbtt_GetCodepointShape(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetCodepointShape(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBTruetype.stbtt_GetCodepointShape(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stbtt_GetCodepointSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,int[],int[],int[],int[])"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetCodepointSDF(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetCodepointBitmapBoxSubpixel(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def stbtt_PackBegin(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackBegin(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,int,int,int)"""
        return bool.__wrap(__STBTruetype.stbtt_PackBegin(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stbtt_PackSetSkipMissingCodepoints(arg0: 'STBTTPackContext', arg1: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_PackSetSkipMissingCodepoints(org.lwjgl.stb.STBTTPackContext,boolean)"""
        __STBTruetype.stbtt_PackSetSkipMissingCodepoints(arg0, __boolean.valueOf(arg1))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBox(long,int,float,float,int[],int[],int[],int[])"""
        __STBTruetype.nstbtt_GetCodepointBitmapBox(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBox(long,int,float,float,int[],int[],int[],int[])"""
        __STBTruetype.nstbtt_GetGlyphBitmapBox(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def stbtt_GetGlyphBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBox(org.lwjgl.stb.STBTTFontinfo,int,int[],int[],int[],int[])"""
        return bool.__wrap(__STBTruetype.stbtt_GetGlyphBox(arg0, __int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetCodepointBitmap(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def nstbtt_InitFont(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_InitFont(long,long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_InitFont(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphSDF(long,float,int,int,byte,float,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphSDF(__long.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_GetGlyphHMetrics(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphHMetrics(long,int,long,long)"""
        __STBTruetype.nstbtt_GetGlyphHMetrics(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def stbtt_FindMatchingFont(arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_FindMatchingFont(java.nio.ByteBuffer,java.nio.ByteBuffer,int)"""
        return int.__wrap(__STBTruetype.stbtt_FindMatchingFont(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetCodepointSVG(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetCodepointSVG(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBTruetype.stbtt_GetCodepointSVG(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def stbtt_GetBakedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: 'FloatBuffer', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetBakedQuad(org.lwjgl.stb.STBTTBakedChar$Buffer,int,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        __STBTruetype.stbtt_GetBakedQuad(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, __boolean.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_Rasterize(arg0: 'STBTTBitmap', arg1: float, arg2: 'Buffer', arg3: float, arg4: float, arg5: float, arg6: float, arg7: int, arg8: int, arg9: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_Rasterize(org.lwjgl.stb.STBTTBitmap,float,org.lwjgl.stb.STBTTVertex$Buffer,float,float,float,float,int,int,boolean)"""
        __STBTruetype.stbtt_Rasterize(arg0, __float.valueOf(arg1), arg2, __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetGlyphBitmapSubpixel(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_PackFontRange(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRange(long,long,int,float,int,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_PackFontRange(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        __STBTruetype.stbtt_MakeCodepointBitmapSubpixelPrefilter(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, arg12, __int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'float', arg12: 'float', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,float[],float[],int)"""
        __STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, arg12, __int.valueOf(arg13))

    @staticmethod
    @overload
    def nstbtt_GetGlyphSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphSDF(long,float,int,int,byte,float,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphSDF(__long.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointKernAdvance(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointKernAdvance(long,int,int)"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointKernAdvance(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_FreeShape(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_FreeShape(long,long)"""
        __STBTruetype.nstbtt_FreeShape(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def nstbtt_GetFontNameString(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetFontNameString(long,long,int,int,int,int)"""
        return int.__wrap(__STBTruetype.nstbtt_GetFontNameString(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def nstbtt_PackFontRanges(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRanges(long,long,int,long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_PackFontRanges(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def stbtt_GetFontVMetricsOS2(arg0: 'STBTTFontinfo', arg1: 'int', arg2: 'int', arg3: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetricsOS2(org.lwjgl.stb.STBTTFontinfo,int[],int[],int[])"""
        return bool.__wrap(__STBTruetype.stbtt_GetFontVMetricsOS2(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBox(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBox(long,int,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointBox(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbtt_GetCodepointKernAdvance(arg0: 'STBTTFontinfo', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetCodepointKernAdvance(org.lwjgl.stb.STBTTFontinfo,int,int)"""
        return int.__wrap(__STBTruetype.stbtt_GetCodepointKernAdvance(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetCodepointBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBox(org.lwjgl.stb.STBTTFontinfo,int,int[],int[],int[],int[])"""
        return bool.__wrap(__STBTruetype.stbtt_GetCodepointBox(arg0, __int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_GetCodepointSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointSDF(long,float,int,int,byte,float,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointSDF(__long.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(long,int,float,float,float,float,long,long,long,long)"""
        __STBTruetype.nstbtt_GetCodepointBitmapBoxSubpixel(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def nstbtt_GetKerningTable(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetKerningTable(long,long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_GetKerningTable(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapSubpixel(long,float,float,float,float,int,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphBitmapSubpixel(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetGlyphBitmapSubpixel(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmapSubpixel(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmapSubpixel(long,long,int,int,int,float,float,float,float,int)"""
        __STBTruetype.nstbtt_MakeGlyphBitmapSubpixel(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_PackFontRange(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: float, arg4: int, arg5: 'Buffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackFontRange(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,float,int,org.lwjgl.stb.STBTTPackedchar$Buffer)"""
        return bool.__wrap(__STBTruetype.stbtt_PackFontRange(arg0, arg1, __int.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), arg5))

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(long,long,int,int,int,float,float,float,float,int,int,long,long,int)"""
        __STBTruetype.nstbtt_MakeGlyphBitmapSubpixelPrefilter(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12), __int.valueOf(arg13))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetGlyphBitmap(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def nstbtt_BakeFontBitmap(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_BakeFontBitmap(long,int,float,long,int,int,int,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_BakeFontBitmap(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetCodepointBitmap(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def stbtt_GetGlyphKernAdvance(arg0: 'STBTTFontinfo', arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetGlyphKernAdvance(org.lwjgl.stb.STBTTFontinfo,int,int)"""
        return int.__wrap(__STBTruetype.stbtt_GetGlyphKernAdvance(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetKerningTableLength(arg0: 'STBTTFontinfo') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetKerningTableLength(org.lwjgl.stb.STBTTFontinfo)"""
        return int.__wrap(__STBTruetype.stbtt_GetKerningTableLength(arg0))

    @staticmethod
    @overload
    def nstbtt_PackEnd(arg0: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackEnd(long)"""
        __STBTruetype.nstbtt_PackEnd(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stbtt_ScaleForPixelHeight(arg0: 'STBTTFontinfo', arg1: float) -> float:
        """public static float org.lwjgl.stb.STBTruetype.stbtt_ScaleForPixelHeight(org.lwjgl.stb.STBTTFontinfo,float)"""
        return float.__wrap(__STBTruetype.stbtt_ScaleForPixelHeight(arg0, __float.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_PackSetOversampling(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackSetOversampling(long,int,int)"""
        __STBTruetype.nstbtt_PackSetOversampling(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmap(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmap(long,long,int,int,int,float,float,int)"""
        __STBTruetype.nstbtt_MakeCodepointBitmap(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBoxSubpixel(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(long,int,float,float,float,float,long,long,long,long)"""
        __STBTruetype.nstbtt_GetGlyphBitmapBoxSubpixel(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def nstbtt_GetGlyphKernAdvance(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphKernAdvance(long,int,int)"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphKernAdvance(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphSVG(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphSVG(long,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphSVG(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetCodepointSDF(arg0: 'STBTTFontinfo', arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointSDF(org.lwjgl.stb.STBTTFontinfo,float,int,int,byte,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetCodepointSDF(arg0, __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def stbtt_FreeBitmap(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeBitmap(java.nio.ByteBuffer,long)"""
        __STBTruetype.stbtt_FreeBitmap(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def stbtt_PackBegin(arg0: 'STBTTPackContext', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackBegin(org.lwjgl.stb.STBTTPackContext,java.nio.ByteBuffer,int,int,int,int,long)"""
        return bool.__wrap(__STBTruetype.stbtt_PackBegin(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmap(long,float,float,int,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphBitmap(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def nstbtt_FindSVGDoc(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_FindSVGDoc(long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_FindSVGDoc(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmap(long,float,float,int,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointBitmap(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def nstbtt_GetPackedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetPackedQuad(long,int,int,int,long,long,long,int)"""
        __STBTruetype.nstbtt_GetPackedQuad(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_PackFontRangesRenderIntoRects(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_PackFontRangesRenderIntoRects(long,long,long,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_PackFontRangesRenderIntoRects(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nstbtt_GetScaledFontVMetrics(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetScaledFontVMetrics(long,int,float,long,long,long)"""
        __STBTruetype.nstbtt_GetScaledFontVMetrics(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def stbtt_InitFont(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_InitFont(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBTruetype.stbtt_InitFont(arg0, arg1))

    @staticmethod
    @overload
    def nstbtt_GetGlyphHMetrics(arg0: int, arg1: int, arg2: 'int', arg3: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphHMetrics(long,int,int[],int[])"""
        __STBTruetype.nstbtt_GetGlyphHMetrics(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmap(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmap(long,float,float,int,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointBitmap(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def stbtt_GetScaledFontVMetrics(arg0: 'ByteBuffer', arg1: int, arg2: float, arg3: 'FloatBuffer', arg4: 'FloatBuffer', arg5: 'FloatBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetScaledFontVMetrics(java.nio.ByteBuffer,int,float,java.nio.FloatBuffer,java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        __STBTruetype.stbtt_GetScaledFontVMetrics(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, arg4, arg5)

    @staticmethod
    @overload
    def nstbtt_MakeCodepointBitmapSubpixel(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeCodepointBitmapSubpixel(long,long,int,int,int,float,float,float,float,int)"""
        __STBTruetype.nstbtt_MakeCodepointBitmapSubpixel(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_GetGlyphShape(arg0: 'STBTTFontinfo', arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphShape(org.lwjgl.stb.STBTTFontinfo,int)"""
        return Buffer.__wrap(__STBTruetype.stbtt_GetGlyphShape(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBoxSubpixel(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(org.lwjgl.stb.STBTTFontinfo,int,float,float,float,float,int[],int[],int[],int[])"""
        __STBTruetype.stbtt_GetGlyphBitmapBoxSubpixel(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9)

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmap(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: int, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmap(org.lwjgl.stb.STBTTFontinfo,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetGlyphBitmap(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, arg7))

    @staticmethod
    @overload
    def stbtt_GetPackedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'FloatBuffer', arg5: 'FloatBuffer', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetPackedQuad(org.lwjgl.stb.STBTTPackedchar$Buffer,int,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        __STBTruetype.stbtt_GetPackedQuad(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, __boolean.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_GetGlyphBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBox(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool.__wrap(__STBTruetype.stbtt_GetGlyphBox(arg0, __int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_GetFontOffsetForIndex(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetFontOffsetForIndex(long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_GetFontOffsetForIndex(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,int[],int[],int[],int[])"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetCodepointBitmapSubpixel(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_CompareUTF8toUTF16_bigendian(arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_CompareUTF8toUTF16_bigendian(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return bool.__wrap(__STBTruetype.stbtt_CompareUTF8toUTF16_bigendian(arg0, arg1))

    @staticmethod
    @overload
    def nstbtt_GetCodepointHMetrics(arg0: int, arg1: int, arg2: 'int', arg3: 'int'):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointHMetrics(long,int,int[],int[])"""
        __STBTruetype.nstbtt_GetCodepointHMetrics(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nstbtt_ScaleForMappingEmToPixels(arg0: int, arg1: float) -> float:
        """public static native float org.lwjgl.stb.STBTruetype.nstbtt_ScaleForMappingEmToPixels(long,float)"""
        return float.__wrap(__STBTruetype.nstbtt_ScaleForMappingEmToPixels(__long.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetKerningTableLength(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetKerningTableLength(long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetKerningTableLength(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stbtt_IsGlyphEmpty(arg0: 'STBTTFontinfo', arg1: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_IsGlyphEmpty(org.lwjgl.stb.STBTTFontinfo,int)"""
        return bool.__wrap(__STBTruetype.stbtt_IsGlyphEmpty(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapSubpixel(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapSubpixel(long,float,float,float,float,int,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointBitmapSubpixel(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBitmapBox(long,int,float,float,long,long,long,long)"""
        __STBTruetype.nstbtt_GetCodepointBitmapBox(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBox(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBox(long,int,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphBox(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_Rasterize(arg0: int, arg1: float, arg2: int, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_Rasterize(long,float,long,int,float,float,float,float,int,int,int,long)"""
        __STBTruetype.nstbtt_Rasterize(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def stbtt_GetGlyphSVG(arg0: 'STBTTFontinfo', arg1: int, arg2: 'PointerBuffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetGlyphSVG(org.lwjgl.stb.STBTTFontinfo,int,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__STBTruetype.stbtt_GetGlyphSVG(arg0, __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nstbtt_GetGlyphBox(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBox(long,int,long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetGlyphBox(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def stbtt_GetGlyphBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'int', arg5: 'int', arg6: 'int', arg7: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,int[],int[],int[],int[])"""
        __STBTruetype.stbtt_GetGlyphBitmapBox(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def stbtt_GetFontOffsetForIndex(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetFontOffsetForIndex(java.nio.ByteBuffer,int)"""
        return int.__wrap(__STBTruetype.stbtt_GetFontOffsetForIndex(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_GetGlyphHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'int', arg3: 'int'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphHMetrics(org.lwjgl.stb.STBTTFontinfo,int,int[],int[])"""
        __STBTruetype.stbtt_GetGlyphHMetrics(arg0, __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def stbtt_InitFont(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int) -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_InitFont(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int)"""
        return bool.__wrap(__STBTruetype.stbtt_InitFont(arg0, arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_GetBakedQuad(arg0: 'Buffer', arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: 'STBTTAlignedQuad', arg7: bool):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetBakedQuad(org.lwjgl.stb.STBTTBakedChar$Buffer,int,int,int,float[],float[],org.lwjgl.stb.STBTTAlignedQuad,boolean)"""
        __STBTruetype.stbtt_GetBakedQuad(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, arg6, __boolean.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_GetFontVMetricsOS2(arg0: 'STBTTFontinfo', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetFontVMetricsOS2(org.lwjgl.stb.STBTTFontinfo,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool.__wrap(__STBTruetype.stbtt_GetFontVMetricsOS2(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbtt_GetCodepointHMetrics(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointHMetrics(long,int,long,long)"""
        __STBTruetype.nstbtt_GetCodepointHMetrics(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nstbtt_MakeGlyphBitmap(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_MakeGlyphBitmap(long,long,int,int,int,float,float,int)"""
        __STBTruetype.nstbtt_MakeGlyphBitmap(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_GetFontVMetricsOS2(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetFontVMetricsOS2(long,long,long,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetFontVMetricsOS2(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nstbtt_GetCodepointSVG(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointSVG(long,int,long)"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointSVG(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int, arg11: 'FloatBuffer', arg12: 'FloatBuffer', arg13: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int,int,java.nio.FloatBuffer,java.nio.FloatBuffer,int)"""
        __STBTruetype.stbtt_MakeGlyphBitmapSubpixelPrefilter(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, arg12, __int.valueOf(arg13))

    @staticmethod
    @overload
    def nstbtt_FindMatchingFont(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_FindMatchingFont(long,long,int)"""
        return int.__wrap(__STBTruetype.nstbtt_FindMatchingFont(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nstbtt_GetBakedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetBakedQuad(long,int,int,int,long,long,long,int)"""
        __STBTruetype.nstbtt_GetBakedQuad(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def nstbtt_PackFontRangesPackRects(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_PackFontRangesPackRects(long,long,int)"""
        __STBTruetype.nstbtt_PackFontRangesPackRects(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def stbtt_GetKerningTable(arg0: 'STBTTFontinfo', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBTruetype.stbtt_GetKerningTable(org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTKerningentry$Buffer)"""
        return int.__wrap(__STBTruetype.stbtt_GetKerningTable(arg0, arg1))

    @staticmethod
    @overload
    def stbtt_FreeBitmap(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_FreeBitmap(java.nio.ByteBuffer)"""
        __STBTruetype.stbtt_FreeBitmap(arg0)

    @staticmethod
    @overload
    def stbtt_GetGlyphHMetrics(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetGlyphHMetrics(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetGlyphHMetrics(arg0, __int.valueOf(arg1), arg2, arg3)

    @staticmethod
    @overload
    def nstbtt_GetGlyphBitmapBox(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetGlyphBitmapBox(long,int,float,float,long,long,long,long)"""
        __STBTruetype.nstbtt_GetGlyphBitmapBox(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stbtt_GetCodepointBox(arg0: 'STBTTFontinfo', arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBox(org.lwjgl.stb.STBTTFontinfo,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return bool.__wrap(__STBTruetype.stbtt_GetCodepointBox(arg0, __int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'IntBuffer', arg7: 'IntBuffer', arg8: 'IntBuffer', arg9: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,float,float,float,float,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        return ByteBuffer.__wrap(__STBTruetype.stbtt_GetCodepointBitmapSubpixel(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetCodepointBitmapBox(arg0: 'STBTTFontinfo', arg1: int, arg2: float, arg3: float, arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'IntBuffer', arg7: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetCodepointBitmapBox(org.lwjgl.stb.STBTTFontinfo,int,float,float,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetCodepointBitmapBox(arg0, __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def nstbtt_GetCodepointSDF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: float, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int') -> int:
        """public static native long org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointSDF(long,float,int,int,byte,float,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointSDF(__long.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8, arg9))

    @staticmethod
    @overload
    def stbtt_GetCodepointShape(arg0: 'STBTTFontinfo', arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTruetype.stbtt_GetCodepointShape(org.lwjgl.stb.STBTTFontinfo,int)"""
        return Buffer.__wrap(__STBTruetype.stbtt_GetCodepointShape(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stbtt_MakeCodepointBitmapSubpixel(arg0: 'STBTTFontinfo', arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_MakeCodepointBitmapSubpixel(org.lwjgl.stb.STBTTFontinfo,java.nio.ByteBuffer,int,int,int,float,float,float,float,int)"""
        __STBTruetype.stbtt_MakeCodepointBitmapSubpixel(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __int.valueOf(arg9))

    @staticmethod
    @overload
    def stbtt_GetFontBoundingBox(arg0: 'STBTTFontinfo', arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetFontBoundingBox(org.lwjgl.stb.STBTTFontinfo,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __STBTruetype.stbtt_GetFontBoundingBox(arg0, arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def nstbtt_GetBakedQuad(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'float', arg6: int, arg7: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetBakedQuad(long,int,int,int,float[],float[],long,int)"""
        __STBTruetype.nstbtt_GetBakedQuad(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6), __int.valueOf(arg7))

    @staticmethod
    @overload
    def stbtt_PackFontRangesRenderIntoRects(arg0: 'STBTTPackContext', arg1: 'STBTTFontinfo', arg2: 'Buffer', arg3: 'Buffer') -> bool:
        """public static boolean org.lwjgl.stb.STBTruetype.stbtt_PackFontRangesRenderIntoRects(org.lwjgl.stb.STBTTPackContext,org.lwjgl.stb.STBTTFontinfo,org.lwjgl.stb.STBTTPackRange$Buffer,org.lwjgl.stb.STBRPRect$Buffer)"""
        return bool.__wrap(__STBTruetype.stbtt_PackFontRangesRenderIntoRects(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def nstbtt_GetFontBoundingBox(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_GetFontBoundingBox(long,long,long,long,long)"""
        __STBTruetype.nstbtt_GetFontBoundingBox(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def stbtt_GetScaledFontVMetrics(arg0: 'ByteBuffer', arg1: int, arg2: float, arg3: 'float', arg4: 'float', arg5: 'float'):
        """public static void org.lwjgl.stb.STBTruetype.stbtt_GetScaledFontVMetrics(java.nio.ByteBuffer,int,float,float[],float[],float[])"""
        __STBTruetype.stbtt_GetScaledFontVMetrics(arg0, __int.valueOf(arg1), __float.valueOf(arg2), arg3, arg4, arg5)

    @staticmethod
    @overload
    def nstbtt_GetCodepointBox(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int') -> int:
        """public static native int org.lwjgl.stb.STBTruetype.nstbtt_GetCodepointBox(long,int,int[],int[],int[],int[])"""
        return int.__wrap(__STBTruetype.nstbtt_GetCodepointBox(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, arg5))

    @staticmethod
    @overload
    def nstbtt_FreeSDF(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBTruetype.nstbtt_FreeSDF(long,long)"""
        __STBTruetype.nstbtt_FreeSDF(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBIReadCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
import org.lwjgl.stb.STBIReadCallback as __STBIReadCallback
__STBIReadCallback = __STBIReadCallback
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.stb.STBIReadCallbackI as __STBIReadCallbackI
__STBIReadCallbackI = __STBIReadCallbackI
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBIReadCallback(ABC):
    """org.lwjgl.stb.STBIReadCallback"""
 
    @staticmethod
    def __wrap(java_value: __STBIReadCallback) -> 'STBIReadCallback':
        return STBIReadCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIReadCallback):
        """
        Dynamic initializer for STBIReadCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIReadCallback.create(long)"""
        return STBIReadCallback.__wrap(__STBIReadCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIReadCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIReadCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIReadCallback.createSafe(long)"""
        return STBIReadCallback.__wrap(__STBIReadCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract int org.lwjgl.stb.STBIReadCallbackI.invoke(long,long,int)"""
        pass

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def getData(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBIReadCallback.getData(long,int)"""
        return ByteBuffer.__wrap(__STBIReadCallback.getData(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIReadCallbackI.callback(long,long)"""
        super(__STBIReadCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'STBIReadCallbackI') -> 'STBIReadCallback':
        """public static org.lwjgl.stb.STBIReadCallback org.lwjgl.stb.STBIReadCallback.create(org.lwjgl.stb.STBIReadCallbackI)"""
        return STBIReadCallback.__wrap(__STBIReadCallback.create(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBTTAlignedQuad
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.stb.STBTTAlignedQuad as __STBTTAlignedQuad
__STBTTAlignedQuad = __STBTTAlignedQuad
import org.lwjgl.stb.STBTTAlignedQuad as __STBTTAlignedQuad_Buffer
__Buffer = __STBTTAlignedQuad_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTAlignedQuad():
    """org.lwjgl.stb.STBTTAlignedQuad"""
 
    @staticmethod
    def __wrap(java_value: __STBTTAlignedQuad) -> 'STBTTAlignedQuad':
        return STBTTAlignedQuad(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTAlignedQuad):
        """
        Dynamic initializer for STBTTAlignedQuad.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.mallocStack(arg0))

    @staticmethod
    @overload
    def ny1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ny1(long)"""
        return float.__wrap(__STBTTAlignedQuad.ny1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.mallocStack()"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.mallocStack())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTAlignedQuad.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.create(int)"""
        return Buffer.__wrap(__STBTTAlignedQuad.create(__int.valueOf(arg0)))

    @overload
    def y1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.y1()"""
        return float.__wrap(super(STBTTAlignedQuad, self).y1())

    @overload
    def s0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.s0()"""
        return float.__wrap(super(STBTTAlignedQuad, self).s0())

    @overload
    def t1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.t1()"""
        return float.__wrap(super(STBTTAlignedQuad, self).t1())

    @overload
    def x0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.x0()"""
        return float.__wrap(super(STBTTAlignedQuad, self).x0())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTAlignedQuad.sizeof()"""
        return int.__wrap(super(STBTTAlignedQuad, self).sizeof())

    @staticmethod
    @overload
    def nx0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nx0(long)"""
        return float.__wrap(__STBTTAlignedQuad.nx0(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.callocStack(int)"""
        return Buffer.__wrap(__STBTTAlignedQuad.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ny0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ny0(long)"""
        return float.__wrap(__STBTTAlignedQuad.ny0(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTAlignedQuad.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.calloc()"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.calloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.create(long)"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ns0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ns0(long)"""
        return float.__wrap(__STBTTAlignedQuad.ns0(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTAlignedQuad(java.nio.ByteBuffer)"""
        val = __STBTTAlignedQuad(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def callocStack() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.callocStack()"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.callocStack())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nt0(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nt0(long)"""
        return float.__wrap(__STBTTAlignedQuad.nt0(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.create(long,int)"""
        return Buffer.__wrap(__STBTTAlignedQuad.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.malloc()"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.malloc())

    @staticmethod
    @overload
    def ns1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.ns1(long)"""
        return float.__wrap(__STBTTAlignedQuad.ns1(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTAlignedQuad.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nt1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nt1(long)"""
        return float.__wrap(__STBTTAlignedQuad.nt1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.calloc(int)"""
        return Buffer.__wrap(__STBTTAlignedQuad.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.calloc(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.mallocStack(int)"""
        return Buffer.__wrap(__STBTTAlignedQuad.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTAlignedQuad.calloc(__int.valueOf(arg0), arg1))

    @overload
    def x1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.x1()"""
        return float.__wrap(super(STBTTAlignedQuad, self).x1())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.callocStack(arg0))

    @overload
    def s1(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.s1()"""
        return float.__wrap(super(STBTTAlignedQuad, self).s1())

    @overload
    def y0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.y0()"""
        return float.__wrap(super(STBTTAlignedQuad, self).y0())

    @staticmethod
    @overload
    def create() -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.create()"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.create())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTAlignedQuad':
        """public static org.lwjgl.stb.STBTTAlignedQuad org.lwjgl.stb.STBTTAlignedQuad.createSafe(long)"""
        return STBTTAlignedQuad.__wrap(__STBTTAlignedQuad.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nx1(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTAlignedQuad.nx1(long)"""
        return float.__wrap(__STBTTAlignedQuad.nx1(__long.valueOf(arg0)))

    @overload
    def t0(self) -> float:
        """public float org.lwjgl.stb.STBTTAlignedQuad.t0()"""
        return float.__wrap(super(STBTTAlignedQuad, self).t0())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.malloc(int)"""
        return Buffer.__wrap(__STBTTAlignedQuad.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTAlignedQuad$Buffer org.lwjgl.stb.STBTTAlignedQuad.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTAlignedQuad.callocStack(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBTTBitmap$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.stb.STBTTBitmap as __STBTTBitmap_Buffer
__Buffer = __STBTTBitmap_Buffer.Buffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTBitmap.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def w(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.w(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).w(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def stride(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap$Buffer.stride()"""
        return int.__wrap(super(Buffer, self).stride())

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTBitmap$Buffer.pixels(int)"""
        return 'ByteBuffer'.__wrap(super(__Buffer, self).pixels(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def h(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.h(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).h(__int.valueOf(arg0)))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBitmap$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def pixels(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.pixels(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).pixels(arg0))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def w(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap$Buffer.w()"""
        return int.__wrap(super(Buffer, self).w())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def h(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap$Buffer.h()"""
        return int.__wrap(super(Buffer, self).h())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTBitmap$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def stride(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap$Buffer.stride(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).stride(__int.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBTTKerningentry$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.stb.STBTTKerningentry as __STBTTKerningentry_Buffer
__Buffer = __STBTTKerningentry_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTKerningentry.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTKerningentry$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def glyph1(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry$Buffer.glyph1()"""
        return int.__wrap(super(Buffer, self).glyph1())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def advance(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry$Buffer.advance()"""
        return int.__wrap(super(Buffer, self).advance())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTKerningentry$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def glyph2(self) -> int:
        """public int org.lwjgl.stb.STBTTKerningentry$Buffer.glyph2()"""
        return int.__wrap(super(Buffer, self).glyph2())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBRPContext$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBRPNode as __STBRPNode_Buffer
__Buffer = __STBRPNode_Buffer.Buffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.stb.STBRPNode as __STBRPNode
__STBRPNode = __STBRPNode
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.stb.STBRPContext as __STBRPContext_Buffer
__Buffer = __STBRPContext_Buffer.Buffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBRPContext.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBRPContext$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def height(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.height()"""
        return int.__wrap(super(Buffer, self).height())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def width(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.width()"""
        return int.__wrap(super(Buffer, self).width())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPContext$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def active_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext$Buffer.active_head()"""
        return 'STBRPNode'.__wrap(super(Buffer, self).active_head())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def init_mode(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.init_mode()"""
        return int.__wrap(super(Buffer, self).init_mode())

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def num_nodes(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.num_nodes()"""
        return int.__wrap(super(Buffer, self).num_nodes())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def extra(self) -> 'Buffer':
        """public org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPContext$Buffer.extra()"""
        return 'Buffer'.__wrap(super(Buffer, self).extra())

    @overload
    def extra(self, arg0: int) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext$Buffer.extra(int)"""
        return 'STBRPNode'.__wrap(super(__Buffer, self).extra(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def free_head(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPContext$Buffer.free_head()"""
        return 'STBRPNode'.__wrap(super(Buffer, self).free_head())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def heuristic(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.heuristic()"""
        return int.__wrap(super(Buffer, self).heuristic())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def align(self) -> int:
        """public int org.lwjgl.stb.STBRPContext$Buffer.align()"""
        return int.__wrap(super(Buffer, self).align())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBIReadCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.stb.STBIReadCallbackI as __STBIReadCallbackI
__STBIReadCallbackI = __STBIReadCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class STBIReadCallbackI(ABC):
    """org.lwjgl.stb.STBIReadCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __STBIReadCallbackI) -> 'STBIReadCallbackI':
        return STBIReadCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIReadCallbackI):
        """
        Dynamic initializer for STBIReadCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIReadCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIReadCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIReadCallbackI.callback(long,long)"""
        super(__STBIReadCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract int org.lwjgl.stb.STBIReadCallbackI.invoke(long,long,int)"""
        pass 
 
 
# CLASS: org.lwjgl.stb.STBPerlin
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import org.lwjgl.stb.STBPerlin as __STBPerlin
__STBPerlin = __STBPerlin
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class STBPerlin():
    """org.lwjgl.stb.STBPerlin"""
 
    @staticmethod
    def __wrap(java_value: __STBPerlin) -> 'STBPerlin':
        return STBPerlin(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBPerlin):
        """
        Dynamic initializer for STBPerlin.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def stb_perlin_turbulence_noise3(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_turbulence_noise3(float,float,float,float,float,int)"""
        return float.__wrap(__STBPerlin.stb_perlin_turbulence_noise3(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stb_perlin_noise3_seed(arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_noise3_seed(float,float,float,int,int,int,int)"""
        return float.__wrap(__STBPerlin.stb_perlin_noise3_seed(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def stb_perlin_noise3(arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_noise3(float,float,float,int,int,int)"""
        return float.__wrap(__STBPerlin.stb_perlin_noise3(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def stb_perlin_noise3_wrap_nonpow2(arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_noise3_wrap_nonpow2(float,float,float,int,int,int,byte)"""
        return float.__wrap(__STBPerlin.stb_perlin_noise3_wrap_nonpow2(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __byte.valueOf(arg6)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stb_perlin_ridge_noise3(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_ridge_noise3(float,float,float,float,float,float,int)"""
        return float.__wrap(__STBPerlin.stb_perlin_ridge_noise3(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __int.valueOf(arg6)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def stb_perlin_fbm_noise3(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int) -> float:
        """public static native float org.lwjgl.stb.STBPerlin.stb_perlin_fbm_noise3(float,float,float,float,float,int)"""
        return float.__wrap(__STBPerlin.stb_perlin_fbm_noise3(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5))) 
 
 
# CLASS: org.lwjgl.stb.STBRPRect
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.stb.STBRPRect as __STBRPRect
__STBRPRect = __STBRPRect
import org.lwjgl.stb.STBRPRect as __STBRPRect_Buffer
__Buffer = __STBRPRect_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBRPRect():
    """org.lwjgl.stb.STBRPRect"""
 
    @staticmethod
    def __wrap(java_value: __STBRPRect) -> 'STBRPRect':
        return STBRPRect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBRPRect):
        """
        Dynamic initializer for STBRPRect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.create(long,int)"""
        return Buffer.__wrap(__STBRPRect.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.createSafe(long)"""
        return STBRPRect.__wrap(__STBRPRect.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPRect.__wrap(__STBRPRect.callocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPRect.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nh(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nh(long,int)"""
        __STBRPRect.nh(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.mallocStack(int)"""
        return Buffer.__wrap(__STBRPRect.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPRect.calloc(__int.valueOf(arg0), arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.malloc(org.lwjgl.system.MemoryStack)"""
        return STBRPRect.__wrap(__STBRPRect.malloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.calloc()"""
        return STBRPRect.__wrap(__STBRPRect.calloc())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.malloc(int)"""
        return Buffer.__wrap(__STBRPRect.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.x()"""
        return int.__wrap(super(STBRPRect, self).x())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.calloc(int)"""
        return Buffer.__wrap(__STBRPRect.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.malloc()"""
        return STBRPRect.__wrap(__STBRPRect.malloc())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPRect(java.nio.ByteBuffer)"""
        val = __STBRPRect(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nwas_packed(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nwas_packed(long,int)"""
        __STBRPRect.nwas_packed(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.createSafe(long,int)"""
        return Buffer.__wrap(__STBRPRect.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPRect.callocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.set(int,int,int,int,int,boolean)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5)))

    @overload
    def set(self, arg0: 'STBRPRect') -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.set(org.lwjgl.stb.STBRPRect)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).set(arg0))

    @staticmethod
    @overload
    def create() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.create()"""
        return STBRPRect.__wrap(__STBRPRect.create())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.ny(long)"""
        return int.__wrap(__STBRPRect.ny(__long.valueOf(arg0)))

    @overload
    def w(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.w()"""
        return int.__wrap(super(STBRPRect, self).w())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def id(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.id(int)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).id(__int.valueOf(arg0)))

    @overload
    def id(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.id()"""
        return int.__wrap(super(STBRPRect, self).id())

    @staticmethod
    @overload
    def mallocStack() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.mallocStack()"""
        return STBRPRect.__wrap(__STBRPRect.mallocStack())

    @overload
    def y(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.y(int)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).y(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack() -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.callocStack()"""
        return STBRPRect.__wrap(__STBRPRect.callocStack())

    @staticmethod
    @overload
    def nx(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nx(long,int)"""
        __STBRPRect.nx(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPRect.__wrap(__STBRPRect.mallocStack(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def ny(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.ny(long,int)"""
        __STBRPRect.ny(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nw(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nw(long,int)"""
        __STBRPRect.nw(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nwas_packed(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nwas_packed(long)"""
        return int.__wrap(__STBRPRect.nwas_packed(__long.valueOf(arg0)))

    @overload
    def was_packed(self) -> bool:
        """public boolean org.lwjgl.stb.STBRPRect.was_packed()"""
        return bool.__wrap(super(STBRPRect, self).was_packed())

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nx(long)"""
        return int.__wrap(__STBRPRect.nx(__long.valueOf(arg0)))

    @overload
    def h(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.h(int)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).h(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.callocStack(int)"""
        return Buffer.__wrap(__STBRPRect.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.create(int)"""
        return Buffer.__wrap(__STBRPRect.create(__int.valueOf(arg0)))

    @overload
    def x(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.x(int)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).x(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.calloc(org.lwjgl.system.MemoryStack)"""
        return STBRPRect.__wrap(__STBRPRect.calloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPRect$Buffer org.lwjgl.stb.STBRPRect.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPRect.mallocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.sizeof()"""
        return int.__wrap(super(STBRPRect, self).sizeof())

    @overload
    def was_packed(self, arg0: bool) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.was_packed(boolean)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).was_packed(__boolean.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.y()"""
        return int.__wrap(super(STBRPRect, self).y())

    @staticmethod
    @overload
    def nid(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nid(long)"""
        return int.__wrap(__STBRPRect.nid(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def w(self, arg0: int) -> 'STBRPRect':
        """public org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.w(int)"""
        return 'STBRPRect'.__wrap(super(__STBRPRect, self).w(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nw(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nw(long)"""
        return int.__wrap(__STBRPRect.nw(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def h(self) -> int:
        """public int org.lwjgl.stb.STBRPRect.h()"""
        return int.__wrap(super(STBRPRect, self).h())

    @staticmethod
    @overload
    def nh(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPRect.nh(long)"""
        return int.__wrap(__STBRPRect.nh(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBRPRect':
        """public static org.lwjgl.stb.STBRPRect org.lwjgl.stb.STBRPRect.create(long)"""
        return STBRPRect.__wrap(__STBRPRect.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nid(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBRPRect.nid(long,int)"""
        __STBRPRect.nid(__long.valueOf(arg0), __int.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBRectPack
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.stb.STBRectPack as __STBRectPack
__STBRectPack = __STBRectPack
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class STBRectPack():
    """org.lwjgl.stb.STBRectPack"""
 
    @staticmethod
    def __wrap(java_value: __STBRectPack) -> 'STBRectPack':
        return STBRectPack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBRectPack):
        """
        Dynamic initializer for STBRectPack.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def stbrp_init_target(arg0: 'STBRPContext', arg1: int, arg2: int, arg3: 'Buffer'):
        """public static void org.lwjgl.stb.STBRectPack.stbrp_init_target(org.lwjgl.stb.STBRPContext,int,int,org.lwjgl.stb.STBRPNode$Buffer)"""
        __STBRectPack.stbrp_init_target(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nstbrp_setup_heuristic(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBRectPack.nstbrp_setup_heuristic(long,int)"""
        __STBRectPack.nstbrp_setup_heuristic(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstbrp_pack_rects(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.stb.STBRectPack.nstbrp_pack_rects(long,long,int)"""
        return int.__wrap(__STBRectPack.nstbrp_pack_rects(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stbrp_pack_rects(arg0: 'STBRPContext', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.stb.STBRectPack.stbrp_pack_rects(org.lwjgl.stb.STBRPContext,org.lwjgl.stb.STBRPRect$Buffer)"""
        return int.__wrap(__STBRectPack.stbrp_pack_rects(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nstbrp_setup_allow_out_of_mem(arg0: int, arg1: int):
        """public static native void org.lwjgl.stb.STBRectPack.nstbrp_setup_allow_out_of_mem(long,int)"""
        __STBRectPack.nstbrp_setup_allow_out_of_mem(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def stbrp_setup_allow_out_of_mem(arg0: 'STBRPContext', arg1: bool):
        """public static void org.lwjgl.stb.STBRectPack.stbrp_setup_allow_out_of_mem(org.lwjgl.stb.STBRPContext,boolean)"""
        __STBRectPack.stbrp_setup_allow_out_of_mem(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nstbrp_init_target(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.stb.STBRectPack.nstbrp_init_target(long,int,int,long,int)"""
        __STBRectPack.nstbrp_init_target(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def stbrp_setup_heuristic(arg0: 'STBRPContext', arg1: int):
        """public static void org.lwjgl.stb.STBRectPack.stbrp_setup_heuristic(org.lwjgl.stb.STBRPContext,int)"""
        __STBRectPack.stbrp_setup_heuristic(arg0, __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBEasyFont
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.lwjgl.stb.STBEasyFont as __STBEasyFont
__STBEasyFont = __STBEasyFont
import java.lang.Object as __Object
__Object = __Object
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class STBEasyFont():
    """org.lwjgl.stb.STBEasyFont"""
 
    @staticmethod
    def __wrap(java_value: __STBEasyFont) -> 'STBEasyFont':
        return STBEasyFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBEasyFont):
        """
        Dynamic initializer for STBEasyFont.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def stb_easy_font_print(arg0: float, arg1: float, arg2: 'CharSequence', arg3: 'ByteBuffer', arg4: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_print(float,float,java.lang.CharSequence,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int.__wrap(__STBEasyFont.stb_easy_font_print(__float.valueOf(arg0), __float.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def stb_easy_font_height(arg0: 'CharSequence') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_height(java.lang.CharSequence)"""
        return int.__wrap(__STBEasyFont.stb_easy_font_height(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def stb_easy_font_print(arg0: float, arg1: float, arg2: 'ByteBuffer', arg3: 'ByteBuffer', arg4: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_print(float,float,java.nio.ByteBuffer,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int.__wrap(__STBEasyFont.stb_easy_font_print(__float.valueOf(arg0), __float.valueOf(arg1), arg2, arg3, arg4))

    @staticmethod
    @overload
    def stb_easy_font_height(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_height(java.nio.ByteBuffer)"""
        return int.__wrap(__STBEasyFont.stb_easy_font_height(arg0))

    @staticmethod
    @overload
    def stb_easy_font_width(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_width(java.nio.ByteBuffer)"""
        return int.__wrap(__STBEasyFont.stb_easy_font_width(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stb_easy_font_spacing(arg0: float):
        """public static native void org.lwjgl.stb.STBEasyFont.stb_easy_font_spacing(float)"""
        __STBEasyFont.stb_easy_font_spacing(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nstb_easy_font_print(arg0: float, arg1: float, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.stb.STBEasyFont.nstb_easy_font_print(float,float,long,long,long,int)"""
        return int.__wrap(__STBEasyFont.nstb_easy_font_print(__float.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nstb_easy_font_width(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBEasyFont.nstb_easy_font_width(long)"""
        return int.__wrap(__STBEasyFont.nstb_easy_font_width(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nstb_easy_font_height(arg0: int) -> int:
        """public static native int org.lwjgl.stb.STBEasyFont.nstb_easy_font_height(long)"""
        return int.__wrap(__STBEasyFont.nstb_easy_font_height(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stb_easy_font_width(arg0: 'CharSequence') -> int:
        """public static int org.lwjgl.stb.STBEasyFont.stb_easy_font_width(java.lang.CharSequence)"""
        return int.__wrap(__STBEasyFont.stb_easy_font_width(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBIEOFCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import org.lwjgl.stb.STBIEOFCallbackI as __STBIEOFCallbackI
__STBIEOFCallbackI = __STBIEOFCallbackI
import java.lang.Long as __long
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class STBIEOFCallbackI(ABC):
    """org.lwjgl.stb.STBIEOFCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __STBIEOFCallbackI) -> 'STBIEOFCallbackI':
        return STBIEOFCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIEOFCallbackI):
        """
        Dynamic initializer for STBIEOFCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract int org.lwjgl.stb.STBIEOFCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIEOFCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIEOFCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIEOFCallbackI.callback(long,long)"""
        super(__STBIEOFCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBTTBitmap
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.stb.STBTTBitmap as __STBTTBitmap_Buffer
__Buffer = __STBTTBitmap_Buffer.Buffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.stb.STBTTBitmap as __STBTTBitmap
__STBTTBitmap = __STBTTBitmap
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTBitmap():
    """org.lwjgl.stb.STBTTBitmap"""
 
    @staticmethod
    def __wrap(java_value: __STBTTBitmap) -> 'STBTTBitmap':
        return STBTTBitmap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTBitmap):
        """
        Dynamic initializer for STBTTBitmap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.callocStack(int)"""
        return Buffer.__wrap(__STBTTBitmap.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nh(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTBitmap.nh(long)"""
        return int.__wrap(__STBTTBitmap.nh(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.set(int,int,int,java.nio.ByteBuffer)"""
        return 'STBTTBitmap'.__wrap(super(__STBTTBitmap, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.create(int)"""
        return Buffer.__wrap(__STBTTBitmap.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap.__wrap(__STBTTBitmap.malloc(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.malloc(int)"""
        return Buffer.__wrap(__STBTTBitmap.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.create(long,int)"""
        return Buffer.__wrap(__STBTTBitmap.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.createSafe(long)"""
        return STBTTBitmap.__wrap(__STBTTBitmap.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nw(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTBitmap.nw(long)"""
        return int.__wrap(__STBTTBitmap.nw(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstride(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBTTBitmap.nstride(long)"""
        return int.__wrap(__STBTTBitmap.nstride(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.mallocStack(int)"""
        return Buffer.__wrap(__STBTTBitmap.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBitmap.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nstride(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTBitmap.nstride(long,int)"""
        __STBTTBitmap.nstride(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.create(long)"""
        return STBTTBitmap.__wrap(__STBTTBitmap.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBitmap.callocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def w(self, arg0: int) -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.w(int)"""
        return 'STBTTBitmap'.__wrap(super(__STBTTBitmap, self).w(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.malloc()"""
        return STBTTBitmap.__wrap(__STBTTBitmap.malloc())

    @overload
    def stride(self, arg0: int) -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.stride(int)"""
        return 'STBTTBitmap'.__wrap(super(__STBTTBitmap, self).stride(__int.valueOf(arg0)))

    @overload
    def pixels(self, arg0: 'ByteBuffer') -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.pixels(java.nio.ByteBuffer)"""
        return 'STBTTBitmap'.__wrap(super(__STBTTBitmap, self).pixels(arg0))

    @staticmethod
    @overload
    def calloc() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.calloc()"""
        return STBTTBitmap.__wrap(__STBTTBitmap.calloc())

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBTTBitmap.pixels(int)"""
        return 'ByteBuffer'.__wrap(super(__STBTTBitmap, self).pixels(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBitmap.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def h(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.h()"""
        return int.__wrap(super(STBTTBitmap, self).h())

    @overload
    def w(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.w()"""
        return int.__wrap(super(STBTTBitmap, self).w())

    @staticmethod
    @overload
    def nh(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTBitmap.nh(long,int)"""
        __STBTTBitmap.nh(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def stride(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.stride()"""
        return int.__wrap(super(STBTTBitmap, self).stride())

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBTTBitmap.npixels(long,java.nio.ByteBuffer)"""
        __STBTTBitmap.npixels(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTBitmap.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap.__wrap(__STBTTBitmap.calloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap.__wrap(__STBTTBitmap.callocStack(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.calloc(int)"""
        return Buffer.__wrap(__STBTTBitmap.calloc(__int.valueOf(arg0)))

    @overload
    def h(self, arg0: int) -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.h(int)"""
        return 'STBTTBitmap'.__wrap(super(__STBTTBitmap, self).h(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBTTBitmap.validate(long)"""
        __STBTTBitmap.validate(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBitmap(java.nio.ByteBuffer)"""
        val = __STBTTBitmap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nw(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTBitmap.nw(long,int)"""
        __STBTTBitmap.nw(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.create()"""
        return STBTTBitmap.__wrap(__STBTTBitmap.create())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTBitmap.__wrap(__STBTTBitmap.mallocStack(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTBitmap$Buffer org.lwjgl.stb.STBTTBitmap.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTBitmap.mallocStack(__int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'STBTTBitmap') -> 'STBTTBitmap':
        """public org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.set(org.lwjgl.stb.STBTTBitmap)"""
        return 'STBTTBitmap'.__wrap(super(__STBTTBitmap, self).set(arg0))

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBTTBitmap.npixels(long,int)"""
        return ByteBuffer.__wrap(__STBTTBitmap.npixels(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTBitmap.sizeof()"""
        return int.__wrap(super(STBTTBitmap, self).sizeof())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.mallocStack()"""
        return STBTTBitmap.__wrap(__STBTTBitmap.mallocStack())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def callocStack() -> 'STBTTBitmap':
        """public static org.lwjgl.stb.STBTTBitmap org.lwjgl.stb.STBTTBitmap.callocStack()"""
        return STBTTBitmap.__wrap(__STBTTBitmap.callocStack()) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisInfo$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import org.lwjgl.stb.STBVorbisInfo as __STBVorbisInfo_Buffer
__Buffer = __STBVorbisInfo_Buffer.Buffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBVorbisInfo.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def setup_temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.setup_temp_memory_required()"""
        return int.__wrap(super(Buffer, self).setup_temp_memory_required())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def channels(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.channels()"""
        return int.__wrap(super(Buffer, self).channels())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def sample_rate(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.sample_rate()"""
        return int.__wrap(super(Buffer, self).sample_rate())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBVorbisInfo$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisInfo$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.temp_memory_required()"""
        return int.__wrap(super(Buffer, self).temp_memory_required())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def max_frame_size(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.max_frame_size()"""
        return int.__wrap(super(Buffer, self).max_frame_size())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def setup_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo$Buffer.setup_memory_required()"""
        return int.__wrap(super(Buffer, self).setup_memory_required())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBIZlibCompressI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.stb.STBIZlibCompressI as __STBIZlibCompressI
__STBIZlibCompressI = __STBIZlibCompressI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class STBIZlibCompressI(ABC):
    """org.lwjgl.stb.STBIZlibCompressI"""
 
    @staticmethod
    def __wrap(java_value: __STBIZlibCompressI) -> 'STBIZlibCompressI':
        return STBIZlibCompressI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIZlibCompressI):
        """
        Dynamic initializer for STBIZlibCompressI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIZlibCompressI.callback(long,long)"""
        super(__STBIZlibCompressI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.stb.STBIZlibCompressI.invoke(long,int,long,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIZlibCompressI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIZlibCompressI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBIEOFCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import org.lwjgl.stb.STBIEOFCallbackI as __STBIEOFCallbackI
__STBIEOFCallbackI = __STBIEOFCallbackI
import org.lwjgl.stb.STBIEOFCallback as __STBIEOFCallback
__STBIEOFCallback = __STBIEOFCallback
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class STBIEOFCallback(ABC):
    """org.lwjgl.stb.STBIEOFCallback"""
 
    @staticmethod
    def __wrap(java_value: __STBIEOFCallback) -> 'STBIEOFCallback':
        return STBIEOFCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIEOFCallback):
        """
        Dynamic initializer for STBIEOFCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIEOFCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIEOFCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIEOFCallback.create(long)"""
        return STBIEOFCallback.__wrap(__STBIEOFCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIEOFCallbackI.callback(long,long)"""
        super(__STBIEOFCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'STBIEOFCallbackI') -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIEOFCallback.create(org.lwjgl.stb.STBIEOFCallbackI)"""
        return STBIEOFCallback.__wrap(__STBIEOFCallback.create(arg0))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract int org.lwjgl.stb.STBIEOFCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIEOFCallback':
        """public static org.lwjgl.stb.STBIEOFCallback org.lwjgl.stb.STBIEOFCallback.createSafe(long)"""
        return STBIEOFCallback.__wrap(__STBIEOFCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBRPNode$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBRPNode as __STBRPNode_Buffer
__Buffer = __STBRPNode_Buffer.Buffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.stb.STBRPNode as __STBRPNode
__STBRPNode = __STBRPNode
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBRPNode.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPNode$Buffer.x()"""
        return int.__wrap(super(Buffer, self).x())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPNode$Buffer.y()"""
        return int.__wrap(super(Buffer, self).y())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def next(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode$Buffer.next()"""
        return 'STBRPNode'.__wrap(super(Buffer, self).next())

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBRPNode$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPNode$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisAlloc
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.stb.STBVorbisAlloc as __STBVorbisAlloc
__STBVorbisAlloc = __STBVorbisAlloc
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.stb.STBVorbisAlloc as __STBVorbisAlloc_Buffer
__Buffer = __STBVorbisAlloc_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBVorbisAlloc():
    """org.lwjgl.stb.STBVorbisAlloc"""
 
    @staticmethod
    def __wrap(java_value: __STBVorbisAlloc) -> 'STBVorbisAlloc':
        return STBVorbisAlloc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBVorbisAlloc):
        """
        Dynamic initializer for STBVorbisAlloc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.calloc(int)"""
        return Buffer.__wrap(__STBVorbisAlloc.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.callocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisAlloc.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.createSafe(long)"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.mallocStack(int)"""
        return Buffer.__wrap(__STBVorbisAlloc.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nalloc_buffer_length_in_bytes(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer_length_in_bytes(long)"""
        return int.__wrap(__STBVorbisAlloc.nalloc_buffer_length_in_bytes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.mallocStack()"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.mallocStack())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.calloc()"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.calloc())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.calloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.calloc(arg0))

    @staticmethod
    @overload
    def callocStack() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.callocStack()"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.callocStack())

    @overload
    def alloc_buffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisAlloc.alloc_buffer()"""
        return 'ByteBuffer'.__wrap(super(STBVorbisAlloc, self).alloc_buffer())

    @staticmethod
    @overload
    def nalloc_buffer(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer(long)"""
        return ByteBuffer.__wrap(__STBVorbisAlloc.nalloc_buffer(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBVorbisAlloc.sizeof()"""
        return int.__wrap(super(STBVorbisAlloc, self).sizeof())

    @overload
    def alloc_buffer(self, arg0: 'ByteBuffer') -> 'STBVorbisAlloc':
        """public org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.alloc_buffer(java.nio.ByteBuffer)"""
        return 'STBVorbisAlloc'.__wrap(super(__STBVorbisAlloc, self).alloc_buffer(arg0))

    @overload
    def set(self, arg0: 'STBVorbisAlloc') -> 'STBVorbisAlloc':
        """public org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.set(org.lwjgl.stb.STBVorbisAlloc)"""
        return 'STBVorbisAlloc'.__wrap(super(__STBVorbisAlloc, self).set(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.create(long)"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.create(long,int)"""
        return Buffer.__wrap(__STBVorbisAlloc.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.mallocStack(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisAlloc.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.create(int)"""
        return Buffer.__wrap(__STBVorbisAlloc.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.callocStack(int)"""
        return Buffer.__wrap(__STBVorbisAlloc.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.stb.STBVorbisAlloc.validate(long)"""
        __STBVorbisAlloc.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisAlloc.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisAlloc(java.nio.ByteBuffer)"""
        val = __STBVorbisAlloc(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.malloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.malloc(arg0))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.createSafe(long,int)"""
        return Buffer.__wrap(__STBVorbisAlloc.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisAlloc.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc.malloc(int)"""
        return Buffer.__wrap(__STBVorbisAlloc.malloc(__int.valueOf(arg0)))

    @overload
    def alloc_buffer_length_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBVorbisAlloc.alloc_buffer_length_in_bytes()"""
        return int.__wrap(super(STBVorbisAlloc, self).alloc_buffer_length_in_bytes())

    @staticmethod
    @overload
    def nalloc_buffer(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer(long,java.nio.ByteBuffer)"""
        __STBVorbisAlloc.nalloc_buffer(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nalloc_buffer_length_in_bytes(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBVorbisAlloc.nalloc_buffer_length_in_bytes(long,int)"""
        __STBVorbisAlloc.nalloc_buffer_length_in_bytes(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.create()"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.create())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc() -> 'STBVorbisAlloc':
        """public static org.lwjgl.stb.STBVorbisAlloc org.lwjgl.stb.STBVorbisAlloc.malloc()"""
        return STBVorbisAlloc.__wrap(__STBVorbisAlloc.malloc()) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisComment$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import org.lwjgl.stb.STBVorbisComment as __STBVorbisComment_Buffer
__Buffer = __STBVorbisComment_Buffer.Buffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBVorbisComment.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def comment_list_length(self) -> int:
        """public int org.lwjgl.stb.STBVorbisComment$Buffer.comment_list_length()"""
        return int.__wrap(super(Buffer, self).comment_list_length())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def comment_list(self) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.stb.STBVorbisComment$Buffer.comment_list()"""
        return 'pygl.PointerBuffer'.__wrap(super(Buffer, self).comment_list())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def vendor(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisComment$Buffer.vendor()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).vendor())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def vendorString(self) -> str:
        """public java.lang.String org.lwjgl.stb.STBVorbisComment$Buffer.vendorString()"""
        return str.__wrap(super(Buffer, self).vendorString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisComment$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBVorbisComment$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.stb.STBVorbisInfo as __STBVorbisInfo
__STBVorbisInfo = __STBVorbisInfo
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.stb.STBVorbisInfo as __STBVorbisInfo_Buffer
__Buffer = __STBVorbisInfo_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBVorbisInfo():
    """org.lwjgl.stb.STBVorbisInfo"""
 
    @staticmethod
    def __wrap(java_value: __STBVorbisInfo) -> 'STBVorbisInfo':
        return STBVorbisInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBVorbisInfo):
        """
        Dynamic initializer for STBVorbisInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.malloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.malloc(arg0))

    @overload
    def sample_rate(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.sample_rate()"""
        return int.__wrap(super(STBVorbisInfo, self).sample_rate())

    @staticmethod
    @overload
    def mallocStack() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.mallocStack()"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.mallocStack())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.createSafe(long)"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.createSafe(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisInfo(java.nio.ByteBuffer)"""
        val = __STBVorbisInfo(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisInfo.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisInfo.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.malloc(int)"""
        return Buffer.__wrap(__STBVorbisInfo.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.create(long,int)"""
        return Buffer.__wrap(__STBVorbisInfo.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nsetup_temp_memory_required(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nsetup_temp_memory_required(long)"""
        return int.__wrap(__STBVorbisInfo.nsetup_temp_memory_required(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntemp_memory_required(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.ntemp_memory_required(long)"""
        return int.__wrap(__STBVorbisInfo.ntemp_memory_required(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.malloc()"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.malloc())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.mallocStack(int)"""
        return Buffer.__wrap(__STBVorbisInfo.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisInfo.malloc(__int.valueOf(arg0), arg1))

    @overload
    def channels(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.channels()"""
        return int.__wrap(super(STBVorbisInfo, self).channels())

    @staticmethod
    @overload
    def nsample_rate(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nsample_rate(long)"""
        return int.__wrap(__STBVorbisInfo.nsample_rate(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setup_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.setup_memory_required()"""
        return int.__wrap(super(STBVorbisInfo, self).setup_memory_required())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.createSafe(long,int)"""
        return Buffer.__wrap(__STBVorbisInfo.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def setup_temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.setup_temp_memory_required()"""
        return int.__wrap(super(STBVorbisInfo, self).setup_temp_memory_required())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.calloc(int)"""
        return Buffer.__wrap(__STBVorbisInfo.calloc(__int.valueOf(arg0)))

    @overload
    def temp_memory_required(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.temp_memory_required()"""
        return int.__wrap(super(STBVorbisInfo, self).temp_memory_required())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.create()"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.create())

    @staticmethod
    @overload
    def nsetup_memory_required(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nsetup_memory_required(long)"""
        return int.__wrap(__STBVorbisInfo.nsetup_memory_required(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.calloc(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.calloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.sizeof()"""
        return int.__wrap(super(STBVorbisInfo, self).sizeof())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.callocStack(arg0))

    @staticmethod
    @overload
    def nmax_frame_size(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nmax_frame_size(long)"""
        return int.__wrap(__STBVorbisInfo.nmax_frame_size(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.calloc()"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.calloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.mallocStack(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBVorbisInfo.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.callocStack(int)"""
        return Buffer.__wrap(__STBVorbisInfo.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nchannels(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBVorbisInfo.nchannels(long)"""
        return int.__wrap(__STBVorbisInfo.nchannels(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.callocStack()"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.callocStack())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBVorbisInfo$Buffer org.lwjgl.stb.STBVorbisInfo.create(int)"""
        return Buffer.__wrap(__STBVorbisInfo.create(__int.valueOf(arg0)))

    @overload
    def max_frame_size(self) -> int:
        """public int org.lwjgl.stb.STBVorbisInfo.max_frame_size()"""
        return int.__wrap(super(STBVorbisInfo, self).max_frame_size())

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBVorbisInfo':
        """public static org.lwjgl.stb.STBVorbisInfo org.lwjgl.stb.STBVorbisInfo.create(long)"""
        return STBVorbisInfo.__wrap(__STBVorbisInfo.create(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.stb.STBTTPackedchar
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.stb.STBTTPackedchar as __STBTTPackedchar
__STBTTPackedchar = __STBTTPackedchar
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import org.lwjgl.stb.STBTTPackedchar as __STBTTPackedchar_Buffer
__Buffer = __STBTTPackedchar_Buffer.Buffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTPackedchar():
    """org.lwjgl.stb.STBTTPackedchar"""
 
    @staticmethod
    def __wrap(java_value: __STBTTPackedchar) -> 'STBTTPackedchar':
        return STBTTPackedchar(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTPackedchar):
        """
        Dynamic initializer for STBTTPackedchar.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.x1()"""
        return int.__wrap(super(STBTTPackedchar, self).x1())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.calloc(int)"""
        return Buffer.__wrap(__STBTTPackedchar.calloc(__int.valueOf(arg0)))

    @overload
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.xadvance()"""
        return float.__wrap(super(STBTTPackedchar, self).xadvance())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackedchar.mallocStack(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTPackedchar(java.nio.ByteBuffer)"""
        val = __STBTTPackedchar(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def y0(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.y0(short)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).y0(__short.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.mallocStack(arg0))

    @overload
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.y1()"""
        return int.__wrap(super(STBTTPackedchar, self).y1())

    @overload
    def yoff(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.yoff(float)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).yoff(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.malloc(int)"""
        return Buffer.__wrap(__STBTTPackedchar.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.malloc(arg0))

    @overload
    def xoff2(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.xoff2(float)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).xoff2(__float.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTPackedchar.sizeof()"""
        return int.__wrap(super(STBTTPackedchar, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.calloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.calloc()"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.calloc())

    @staticmethod
    @overload
    def nx1(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.nx1(long,short)"""
        __STBTTPackedchar.nx1(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def ny0(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.ny0(long,short)"""
        __STBTTPackedchar.ny0(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.create(int)"""
        return Buffer.__wrap(__STBTTPackedchar.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nx0(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.nx0(long,short)"""
        __STBTTPackedchar.nx0(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def xadvance(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.xadvance(float)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).xadvance(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.malloc()"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.malloc())

    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.xoff()"""
        return float.__wrap(super(STBTTPackedchar, self).xoff())

    @staticmethod
    @overload
    def nyoff(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nyoff(long,float)"""
        __STBTTPackedchar.nyoff(__long.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def callocStack() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.callocStack()"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.callocStack())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackedchar.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.x0()"""
        return int.__wrap(super(STBTTPackedchar, self).x0())

    @staticmethod
    @overload
    def nxadvance(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nxadvance(long)"""
        return float.__wrap(__STBTTPackedchar.nxadvance(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nyoff2(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nyoff2(long)"""
        return float.__wrap(__STBTTPackedchar.nyoff2(__long.valueOf(arg0)))

    @overload
    def x0(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.x0(short)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).x0(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nxoff(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nxoff(long,float)"""
        __STBTTPackedchar.nxoff(__long.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def yoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.yoff2()"""
        return float.__wrap(super(STBTTPackedchar, self).yoff2())

    @overload
    def xoff(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.xoff(float)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).xoff(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nxoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nxoff(long)"""
        return float.__wrap(__STBTTPackedchar.nxoff(__long.valueOf(arg0)))

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTPackedchar.y0()"""
        return int.__wrap(super(STBTTPackedchar, self).y0())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.set(short,short,short,short,float,float,float,float,float)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).set(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8)))

    @staticmethod
    @overload
    def nyoff(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nyoff(long)"""
        return float.__wrap(__STBTTPackedchar.nyoff(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def set(self, arg0: 'STBTTPackedchar') -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.set(org.lwjgl.stb.STBTTPackedchar)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).set(arg0))

    @staticmethod
    @overload
    def nyoff2(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nyoff2(long,float)"""
        __STBTTPackedchar.nyoff2(__long.valueOf(arg0), __float.valueOf(arg1))

    @staticmethod
    @overload
    def ny1(arg0: int, arg1: int):
        """public static void org.lwjgl.stb.STBTTPackedchar.ny1(long,short)"""
        __STBTTPackedchar.ny1(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def nxoff2(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nxoff2(long,float)"""
        __STBTTPackedchar.nxoff2(__long.valueOf(arg0), __float.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTPackedchar.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackedchar.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def x1(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.x1(short)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).x1(__short.valueOf(arg0)))

    @overload
    def xoff2(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.xoff2()"""
        return float.__wrap(super(STBTTPackedchar, self).xoff2())

    @staticmethod
    @overload
    def nxoff2(arg0: int) -> float:
        """public static float org.lwjgl.stb.STBTTPackedchar.nxoff2(long)"""
        return float.__wrap(__STBTTPackedchar.nxoff2(__long.valueOf(arg0)))

    @overload
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTPackedchar.yoff()"""
        return float.__wrap(super(STBTTPackedchar, self).yoff())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTPackedchar.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.mallocStack()"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.mallocStack())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def yoff2(self, arg0: float) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.yoff2(float)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).yoff2(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def ny1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.ny1(long)"""
        return int.__wrap(__STBTTPackedchar.ny1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.createSafe(long)"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.callocStack(int)"""
        return Buffer.__wrap(__STBTTPackedchar.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ny0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.ny0(long)"""
        return int.__wrap(__STBTTPackedchar.ny0(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nx1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.nx1(long)"""
        return int.__wrap(__STBTTPackedchar.nx1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.create(long,int)"""
        return Buffer.__wrap(__STBTTPackedchar.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.create()"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.create())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTPackedchar$Buffer org.lwjgl.stb.STBTTPackedchar.mallocStack(int)"""
        return Buffer.__wrap(__STBTTPackedchar.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.callocStack(arg0))

    @staticmethod
    @overload
    def nx0(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTPackedchar.nx0(long)"""
        return int.__wrap(__STBTTPackedchar.nx0(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTPackedchar':
        """public static org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.create(long)"""
        return STBTTPackedchar.__wrap(__STBTTPackedchar.create(__long.valueOf(arg0)))

    @overload
    def y1(self, arg0: int) -> 'STBTTPackedchar':
        """public org.lwjgl.stb.STBTTPackedchar org.lwjgl.stb.STBTTPackedchar.y1(short)"""
        return 'STBTTPackedchar'.__wrap(super(__STBTTPackedchar, self).y1(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nxadvance(arg0: int, arg1: float):
        """public static void org.lwjgl.stb.STBTTPackedchar.nxadvance(long,float)"""
        __STBTTPackedchar.nxadvance(__long.valueOf(arg0), __float.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBRPNode
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBRPNode as __STBRPNode_Buffer
__Buffer = __STBRPNode_Buffer.Buffer
import org.lwjgl.stb.STBRPNode as __STBRPNode
__STBRPNode = __STBRPNode
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBRPNode():
    """org.lwjgl.stb.STBRPNode"""
 
    @staticmethod
    def __wrap(java_value: __STBRPNode) -> 'STBRPNode':
        return STBRPNode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBRPNode):
        """
        Dynamic initializer for STBRPNode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.mallocStack(int)"""
        return Buffer.__wrap(__STBRPNode.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.malloc(int)"""
        return Buffer.__wrap(__STBRPNode.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPNode.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def y(self) -> int:
        """public int org.lwjgl.stb.STBRPNode.y()"""
        return int.__wrap(super(STBRPNode, self).y())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.calloc(org.lwjgl.system.MemoryStack)"""
        return STBRPNode.__wrap(__STBRPNode.calloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.create(int)"""
        return Buffer.__wrap(__STBRPNode.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.create()"""
        return STBRPNode.__wrap(__STBRPNode.create())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPNode.__wrap(__STBRPNode.mallocStack(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.create(long,int)"""
        return Buffer.__wrap(__STBRPNode.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.malloc()"""
        return STBRPNode.__wrap(__STBRPNode.malloc())

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPNode.nx(long)"""
        return int.__wrap(__STBRPNode.nx(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.callocStack()"""
        return STBRPNode.__wrap(__STBRPNode.callocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.callocStack(int)"""
        return Buffer.__wrap(__STBRPNode.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.calloc(int)"""
        return Buffer.__wrap(__STBRPNode.calloc(__int.valueOf(arg0)))

    @overload
    def next(self) -> 'STBRPNode':
        """public org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.next()"""
        return 'STBRPNode'.__wrap(super(STBRPNode, self).next())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.createSafe(long)"""
        return STBRPNode.__wrap(__STBRPNode.createSafe(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBRPNode(java.nio.ByteBuffer)"""
        val = __STBRPNode(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPNode.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.create(long)"""
        return STBRPNode.__wrap(__STBRPNode.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.mallocStack()"""
        return STBRPNode.__wrap(__STBRPNode.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBRPNode.__wrap(__STBRPNode.callocStack(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def calloc() -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.calloc()"""
        return STBRPNode.__wrap(__STBRPNode.calloc())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nnext(arg0: int) -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.nnext(long)"""
        return STBRPNode.__wrap(__STBRPNode.nnext(__long.valueOf(arg0)))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.stb.STBRPNode.x()"""
        return int.__wrap(super(STBRPNode, self).x())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPNode.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.stb.STBRPNode.ny(long)"""
        return int.__wrap(__STBRPNode.ny(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.createSafe(long,int)"""
        return Buffer.__wrap(__STBRPNode.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBRPNode':
        """public static org.lwjgl.stb.STBRPNode org.lwjgl.stb.STBRPNode.malloc(org.lwjgl.system.MemoryStack)"""
        return STBRPNode.__wrap(__STBRPNode.malloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBRPNode.sizeof()"""
        return int.__wrap(super(STBRPNode, self).sizeof())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBRPNode$Buffer org.lwjgl.stb.STBRPNode.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBRPNode.malloc(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: org.lwjgl.stb.STBTTVertex
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.stb.STBTTVertex as __STBTTVertex
__STBTTVertex = __STBTTVertex
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import org.lwjgl.stb.STBTTVertex as __STBTTVertex_Buffer
__Buffer = __STBTTVertex_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class STBTTVertex():
    """org.lwjgl.stb.STBTTVertex"""
 
    @staticmethod
    def __wrap(java_value: __STBTTVertex) -> 'STBTTVertex':
        return STBTTVertex(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBTTVertex):
        """
        Dynamic initializer for STBTTVertex.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTVertex.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTVertex(java.nio.ByteBuffer)"""
        val = __STBTTVertex(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.calloc()"""
        return STBTTVertex.__wrap(__STBTTVertex.calloc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.create(int)"""
        return Buffer.__wrap(__STBTTVertex.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTVertex.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.calloc(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex.__wrap(__STBTTVertex.calloc(arg0))

    @overload
    def cx(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cx()"""
        return int.__wrap(super(STBTTVertex, self).cx())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.mallocStack(int)"""
        return Buffer.__wrap(__STBTTVertex.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTVertex.malloc(__int.valueOf(arg0), arg1))

    @overload
    def type(self) -> int:
        """public byte org.lwjgl.stb.STBTTVertex.type()"""
        return int.__wrap(super(STBTTVertex, self).type())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.malloc(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex.__wrap(__STBTTVertex.malloc(arg0))

    @staticmethod
    @overload
    def mallocStack() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.mallocStack()"""
        return STBTTVertex.__wrap(__STBTTVertex.mallocStack())

    @staticmethod
    @overload
    def callocStack() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.callocStack()"""
        return STBTTVertex.__wrap(__STBTTVertex.callocStack())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.calloc(int)"""
        return Buffer.__wrap(__STBTTVertex.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.createSafe(long)"""
        return STBTTVertex.__wrap(__STBTTVertex.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.createSafe(long,int)"""
        return Buffer.__wrap(__STBTTVertex.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.create(long)"""
        return STBTTVertex.__wrap(__STBTTVertex.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def ncx(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncx(long)"""
        return int.__wrap(__STBTTVertex.ncx(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__STBTTVertex.mallocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def cy(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cy()"""
        return int.__wrap(super(STBTTVertex, self).cy())

    @overload
    def x(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.x()"""
        return int.__wrap(super(STBTTVertex, self).x())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.create(long,int)"""
        return Buffer.__wrap(__STBTTVertex.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.malloc()"""
        return STBTTVertex.__wrap(__STBTTVertex.malloc())

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ny(long)"""
        return int.__wrap(__STBTTVertex.ny(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.mallocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex.__wrap(__STBTTVertex.mallocStack(arg0))

    @staticmethod
    @overload
    def ncy(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncy(long)"""
        return int.__wrap(__STBTTVertex.ncy(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.stb.STBTTVertex.sizeof()"""
        return int.__wrap(super(STBTTVertex, self).sizeof())

    @overload
    def cy1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cy1()"""
        return int.__wrap(super(STBTTVertex, self).cy1())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create() -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.create()"""
        return STBTTVertex.__wrap(__STBTTVertex.create())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.malloc(int)"""
        return Buffer.__wrap(__STBTTVertex.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncx1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncx1(long)"""
        return int.__wrap(__STBTTVertex.ncx1(__long.valueOf(arg0)))

    @overload
    def cx1(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.cx1()"""
        return int.__wrap(super(STBTTVertex, self).cx1())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.nx(long)"""
        return int.__wrap(__STBTTVertex.nx(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntype(arg0: int) -> int:
        """public static byte org.lwjgl.stb.STBTTVertex.ntype(long)"""
        return int.__wrap(__STBTTVertex.ntype(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.stb.STBTTVertex$Buffer org.lwjgl.stb.STBTTVertex.callocStack(int)"""
        return Buffer.__wrap(__STBTTVertex.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncy1(arg0: int) -> int:
        """public static short org.lwjgl.stb.STBTTVertex.ncy1(long)"""
        return int.__wrap(__STBTTVertex.ncy1(__long.valueOf(arg0)))

    @overload
    def y(self) -> int:
        """public short org.lwjgl.stb.STBTTVertex.y()"""
        return int.__wrap(super(STBTTVertex, self).y())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'STBTTVertex':
        """public static org.lwjgl.stb.STBTTVertex org.lwjgl.stb.STBTTVertex.callocStack(org.lwjgl.system.MemoryStack)"""
        return STBTTVertex.__wrap(__STBTTVertex.callocStack(arg0)) 
 
 
# CLASS: org.lwjgl.stb.STBTTBakedChar$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.stb.STBTTBakedChar as __STBTTBakedChar_Buffer
__Buffer = __STBTTBakedChar_Buffer.Buffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTBakedChar.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def xadvance(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar$Buffer.xadvance()"""
        return float.__wrap(super(Buffer, self).xadvance())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTBakedChar$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def yoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar$Buffer.yoff()"""
        return float.__wrap(super(Buffer, self).yoff())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def y1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.y1()"""
        return int.__wrap(super(Buffer, self).y1())

    @overload
    def x0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.x0()"""
        return int.__wrap(super(Buffer, self).x0())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def y0(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.y0()"""
        return int.__wrap(super(Buffer, self).y0())

    @overload
    def xoff(self) -> float:
        """public float org.lwjgl.stb.STBTTBakedChar$Buffer.xoff()"""
        return float.__wrap(super(Buffer, self).xoff())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTBakedChar$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def x1(self) -> int:
        """public short org.lwjgl.stb.STBTTBakedChar$Buffer.x1()"""
        return int.__wrap(super(Buffer, self).x1()) 
 
 
# CLASS: org.lwjgl.stb.STBIZlibCompress
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.stb.STBIZlibCompress as __STBIZlibCompress
__STBIZlibCompress = __STBIZlibCompress
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.stb.STBIZlibCompressI as __STBIZlibCompressI
__STBIZlibCompressI = __STBIZlibCompressI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class STBIZlibCompress(ABC):
    """org.lwjgl.stb.STBIZlibCompress"""
 
    @staticmethod
    def __wrap(java_value: __STBIZlibCompress) -> 'STBIZlibCompress':
        return STBIZlibCompress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIZlibCompress):
        """
        Dynamic initializer for STBIZlibCompress.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int) -> 'STBIZlibCompress':
        """public static org.lwjgl.stb.STBIZlibCompress org.lwjgl.stb.STBIZlibCompress.create(long)"""
        return STBIZlibCompress.__wrap(__STBIZlibCompress.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIZlibCompressI.callback(long,long)"""
        super(__STBIZlibCompressI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: 'STBIZlibCompressI') -> 'STBIZlibCompress':
        """public static org.lwjgl.stb.STBIZlibCompress org.lwjgl.stb.STBIZlibCompress.create(org.lwjgl.stb.STBIZlibCompressI)"""
        return STBIZlibCompress.__wrap(__STBIZlibCompress.create(arg0))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.stb.STBIZlibCompressI.invoke(long,int,long,int)"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIZlibCompressI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIZlibCompressI, self).getCallInterface())

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'STBIZlibCompress':
        """public static org.lwjgl.stb.STBIZlibCompress org.lwjgl.stb.STBIZlibCompress.createSafe(long)"""
        return STBIZlibCompress.__wrap(__STBIZlibCompress.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.stb.STBTTFontinfo$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.stb.STBTTFontinfo as __STBTTFontinfo_Buffer
__Buffer = __STBTTFontinfo_Buffer.Buffer
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBTTFontinfo.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBTTFontinfo$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBTTFontinfo$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.stb.STBIWriteCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
from pyquantum_helper import override
import org.lwjgl.stb.STBIWriteCallbackI as __STBIWriteCallbackI
__STBIWriteCallbackI = __STBIWriteCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class STBIWriteCallbackI(ABC):
    """org.lwjgl.stb.STBIWriteCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __STBIWriteCallbackI) -> 'STBIWriteCallbackI':
        return STBIWriteCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __STBIWriteCallbackI):
        """
        Dynamic initializer for STBIWriteCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.stb.STBIWriteCallbackI.callback(long,long)"""
        super(__STBIWriteCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.stb.STBIWriteCallbackI.invoke(long,long,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.stb.STBIWriteCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(STBIWriteCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.stb.STBVorbisAlloc$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.stb.STBVorbisAlloc as __STBVorbisAlloc_Buffer
__Buffer = __STBVorbisAlloc_Buffer.Buffer
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class Buffer():
    """org.lwjgl.stb.STBVorbisAlloc.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.stb.STBVorbisAlloc$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def alloc_buffer_length_in_bytes(self) -> int:
        """public int org.lwjgl.stb.STBVorbisAlloc$Buffer.alloc_buffer_length_in_bytes()"""
        return int.__wrap(super(Buffer, self).alloc_buffer_length_in_bytes())

    @overload
    def alloc_buffer(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.stb.STBVorbisAlloc$Buffer org.lwjgl.stb.STBVorbisAlloc$Buffer.alloc_buffer(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).alloc_buffer(arg0))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def alloc_buffer(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.stb.STBVorbisAlloc$Buffer.alloc_buffer()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).alloc_buffer())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.stb.STBVorbisAlloc$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))