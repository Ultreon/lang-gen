from __future__ import annotations
from overload import overload


 
from builtins import str
import com.badlogic.gdx.graphics.GL31 as __GL31
__GL31 = __GL31
import com.badlogic.gdx.graphics.GL30 as __GL30
__GL30 = __GL30
import java.nio.IntBuffer as IntBuffer
import java.nio.Buffer as Buffer
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
from builtins import float
import java.nio.LongBuffer as LongBuffer
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
 
class GL31(ABC, __GL30, GL30):
    """com.badlogic.gdx.graphics.GL31"""
 
    @staticmethod
    def __wrap(java_value: __GL31) -> 'GL31':
        return GL31(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL31):
        """
        Dynamic initializer for GL31.
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
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawElementsInstanced(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glFramebufferParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindTransformFeedback(int,int)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glResumeTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glResumeTransformFeedback()"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2ui(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsTransformFeedback(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsTransformFeedback(int)"""
        pass

    @abstractmethod
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawElementsIndirect(int,int,long)"""
        pass

    @abstractmethod
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawArraysInstanced(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformBlockBinding(int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1i(int,int,int)"""
        pass

    @abstractmethod
    def glBeginTransformFeedback(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginTransformFeedback(int)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glBindVertexArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindVertexArray(int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glEndQuery(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndQuery(int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glBindSampler(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindSampler(int,int)"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4f(int,int,float,float,float,float)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3f(int,int,float,float,float)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glMapBufferRange(int,int,int,int)"""
        pass

    @abstractmethod
    def glBindProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfi(int,int,float,int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glProgramParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindVertexBuffer(int,int,long,int)"""
        pass

    @abstractmethod
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawArraysIndirect(int,long)"""
        pass

    @abstractmethod
    def glSampleMaski(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glSampleMaski(int,int)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glIsSampler(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsSampler(int)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUnmapBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glUnmapBuffer(int)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glDispatchComputeIndirect(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchComputeIndirect(long)"""
        pass

    @abstractmethod
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribFormat(int,int,int,boolean,int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        pass

    @abstractmethod
    def glReadBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glReadBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsQuery(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsQuery(int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2i(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public abstract void com.badlogic.gdx.graphics.GL31.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        pass

    @abstractmethod
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramResourceName(int,int,int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceIndex(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformBlockIndex(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetUniformBlockIndex(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribIPointer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBeginQuery(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginQuery(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1f(int,int,float)"""
        pass

    @abstractmethod
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4i(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramPipelineInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramPipelineInfoLog(int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        pass

    @abstractmethod
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glActiveShaderProgram(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4ui(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsProgramPipeline(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL31.glIsProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetInteger64v(int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetStringi(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetStringi(int,int)"""
        pass

    @abstractmethod
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyBufferSubData(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glEndTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndTransformFeedback()"""
        pass

    @abstractmethod
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetFragDataLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetFragDataLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2f(int,int,float,float)"""
        pass

    @abstractmethod
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glUseProgramStages(int,int,int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribBinding(int,int)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsVertexArray(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsVertexArray(int)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1ui(int,int,int)"""
        pass

    @abstractmethod
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexBindingDivisor(int,int)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String'):
        """public abstract int com.badlogic.gdx.graphics.GL31.glCreateShaderProgramv(int,java.lang.String[])"""
        pass

    @abstractmethod
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchCompute(int,int,int)"""
        pass

    @abstractmethod
    def glPauseTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glPauseTransformFeedback()"""
        pass

    @abstractmethod
    def glMemoryBarrier(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrier(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glMemoryBarrierByRegion(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrierByRegion(int)"""
        pass

    @abstractmethod
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFlushMappedBufferRange(int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glValidateProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glValidateProgramPipeline(int)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferBase(int,int,int)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFramebufferTextureLayer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribDivisor(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribIFormat(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetBufferPointerv(self, arg0: int, arg1: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glGetBufferPointerv(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass

    @abstractmethod
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteri(int,int,int)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.GL31
from builtins import str
import com.badlogic.gdx.graphics.GL31 as __GL31
__GL31 = __GL31
import com.badlogic.gdx.graphics.GL30 as __GL30
__GL30 = __GL30
import java.nio.IntBuffer as IntBuffer
import java.nio.Buffer as Buffer
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
from builtins import float
import java.nio.LongBuffer as LongBuffer
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
 
class GL31(ABC, __GL30, GL30):
    """com.badlogic.gdx.graphics.GL31"""
 
    @staticmethod
    def __wrap(java_value: __GL31) -> 'GL31':
        return GL31(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL31):
        """
        Dynamic initializer for GL31.
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
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawElementsInstanced(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glFramebufferParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindTransformFeedback(int,int)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glResumeTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glResumeTransformFeedback()"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2ui(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsTransformFeedback(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsTransformFeedback(int)"""
        pass

    @abstractmethod
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawElementsIndirect(int,int,long)"""
        pass

    @abstractmethod
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawArraysInstanced(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformBlockBinding(int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1i(int,int,int)"""
        pass

    @abstractmethod
    def glBeginTransformFeedback(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginTransformFeedback(int)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glBindVertexArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindVertexArray(int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glEndQuery(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndQuery(int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glBindSampler(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindSampler(int,int)"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4f(int,int,float,float,float,float)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3f(int,int,float,float,float)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glMapBufferRange(int,int,int,int)"""
        pass

    @abstractmethod
    def glBindProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfi(int,int,float,int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glProgramParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindVertexBuffer(int,int,long,int)"""
        pass

    @abstractmethod
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawArraysIndirect(int,long)"""
        pass

    @abstractmethod
    def glSampleMaski(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glSampleMaski(int,int)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glIsSampler(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsSampler(int)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUnmapBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glUnmapBuffer(int)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glDispatchComputeIndirect(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchComputeIndirect(long)"""
        pass

    @abstractmethod
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribFormat(int,int,int,boolean,int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        pass

    @abstractmethod
    def glReadBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glReadBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsQuery(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsQuery(int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2i(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public abstract void com.badlogic.gdx.graphics.GL31.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        pass

    @abstractmethod
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramResourceName(int,int,int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceIndex(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformBlockIndex(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetUniformBlockIndex(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribIPointer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBeginQuery(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginQuery(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1f(int,int,float)"""
        pass

    @abstractmethod
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4i(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramPipelineInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramPipelineInfoLog(int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        pass

    @abstractmethod
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glActiveShaderProgram(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4ui(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsProgramPipeline(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL31.glIsProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetInteger64v(int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetStringi(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetStringi(int,int)"""
        pass

    @abstractmethod
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyBufferSubData(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glEndTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndTransformFeedback()"""
        pass

    @abstractmethod
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetFragDataLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetFragDataLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2f(int,int,float,float)"""
        pass

    @abstractmethod
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glUseProgramStages(int,int,int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribBinding(int,int)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsVertexArray(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsVertexArray(int)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1ui(int,int,int)"""
        pass

    @abstractmethod
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexBindingDivisor(int,int)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String'):
        """public abstract int com.badlogic.gdx.graphics.GL31.glCreateShaderProgramv(int,java.lang.String[])"""
        pass

    @abstractmethod
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchCompute(int,int,int)"""
        pass

    @abstractmethod
    def glPauseTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glPauseTransformFeedback()"""
        pass

    @abstractmethod
    def glMemoryBarrier(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrier(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glMemoryBarrierByRegion(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrierByRegion(int)"""
        pass

    @abstractmethod
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFlushMappedBufferRange(int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glValidateProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glValidateProgramPipeline(int)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferBase(int,int,int)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFramebufferTextureLayer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribDivisor(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribIFormat(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetBufferPointerv(self, arg0: int, arg1: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glGetBufferPointerv(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass

    @abstractmethod
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteri(int,int,int)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.GL31 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_DownloadPixmapResponseListener
__DownloadPixmapResponseListener = __Pixmap_DownloadPixmapResponseListener.DownloadPixmapResponseListener
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class DownloadPixmapResponseListener(ABC):
    """com.badlogic.gdx.graphics.Pixmap.DownloadPixmapResponseListener"""
 
    @staticmethod
    def __wrap(java_value: __DownloadPixmapResponseListener) -> 'DownloadPixmapResponseListener':
        return DownloadPixmapResponseListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DownloadPixmapResponseListener):
        """
        Dynamic initializer for DownloadPixmapResponseListener.
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
    def downloadFailed(self, arg0: 'Throwable'):
        """public abstract void com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener.downloadFailed(java.lang.Throwable)"""
        pass

    @abstractmethod
    def downloadComplete(self, arg0: 'Pixmap'):
        """public abstract void com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener.downloadComplete(com.badlogic.gdx.graphics.Pixmap)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Filter
__Filter = __Pixmap_Filter.Filter
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Blending
__Blending = __Pixmap_Blending.Blending
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class Pixmap(pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.Pixmap"""
 
    @staticmethod
    def __wrap(java_value: __Pixmap) -> 'Pixmap':
        return Pixmap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pixmap):
        """
        Dynamic initializer for Pixmap.
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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.Pixmap.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Pixmap, self).setColor(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPixel(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getPixel(int,int)"""
        return int.__wrap(super(__Pixmap, self).getPixel(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def fillTriangle(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public void com.badlogic.gdx.graphics.Pixmap.fillTriangle(int,int,int,int,int,int)"""
        super(__Pixmap, self).fillTriangle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getHeight()"""
        return int.__wrap(super(Pixmap, self).getHeight())

    @overload
    def getGLInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getGLInternalFormat()"""
        return int.__wrap(super(Pixmap, self).getGLInternalFormat())

    @overload
    def drawPixel(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixel(int,int)"""
        super(__Pixmap, self).drawPixel(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def downloadFromUrl(arg0: str, arg1: 'DownloadPixmapResponseListener'):
        """public static void com.badlogic.gdx.graphics.Pixmap.downloadFromUrl(java.lang.String,com.badlogic.gdx.graphics.Pixmap$DownloadPixmapResponseListener)"""
        __Pixmap.downloadFromUrl(arg0, arg1)

    @overload
    def setBlending(self, arg0: 'Blending'):
        """public void com.badlogic.gdx.graphics.Pixmap.setBlending(com.badlogic.gdx.graphics.Pixmap$Blending)"""
        super(__Pixmap, self).setBlending(arg0)

    @overload
    def drawRectangle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawRectangle(int,int,int,int)"""
        super(__Pixmap, self).drawRectangle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def getPixels(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.Pixmap.getPixels()"""
        return 'ByteBuffer'.__wrap(super(Pixmap, self).getPixels())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Pixmap.setColor(float,float,float,float)"""
        super(__Pixmap, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getGLType()"""
        return int.__wrap(super(Pixmap, self).getGLType())

    @overload
    def getGLFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getGLFormat()"""
        return int.__wrap(super(Pixmap, self).getGLFormat())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.Pixmap(com.badlogic.gdx.files.FileHandle)"""
        val = __Pixmap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def fill(self):
        """public void com.badlogic.gdx.graphics.Pixmap.fill()"""
        super(Pixmap, self).fill()

    @overload
    def drawPixel(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixel(int,int,int)"""
        super(__Pixmap, self).drawPixel(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def createFromFrameBuffer(arg0: int, arg1: int, arg2: int, arg3: int) -> 'Pixmap':
        """public static com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.Pixmap.createFromFrameBuffer(int,int,int,int)"""
        return Pixmap.__wrap(__Pixmap.createFromFrameBuffer(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def setColor(self, arg0: int):
        """public void com.badlogic.gdx.graphics.Pixmap.setColor(int)"""
        super(__Pixmap, self).setColor(__int.valueOf(arg0))

    @overload
    def getFormat(self) -> 'Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.Pixmap.getFormat()"""
        return 'Format'.__wrap(super(Pixmap, self).getFormat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.Pixmap(java.nio.ByteBuffer,int,int)"""
        val = __Pixmap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def drawPixmap(self, arg0: 'Pixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixmap(com.badlogic.gdx.graphics.Pixmap,int,int,int,int,int,int,int,int)"""
        super(__Pixmap, self).drawPixmap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @overload
    def setPixels(self, arg0: 'ByteBuffer'):
        """public void com.badlogic.gdx.graphics.Pixmap.setPixels(java.nio.ByteBuffer)"""
        super(__Pixmap, self).setPixels(arg0)

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Pixmap.getWidth()"""
        return int.__wrap(super(Pixmap, self).getWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getBlending(self) -> 'Blending':
        """public com.badlogic.gdx.graphics.Pixmap$Blending com.badlogic.gdx.graphics.Pixmap.getBlending()"""
        return 'Blending'.__wrap(super(Pixmap, self).getBlending())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format'):
        """public com.badlogic.gdx.graphics.Pixmap(int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = __Pixmap(__int.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Pixmap.dispose()"""
        super(Pixmap, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def fillRectangle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Pixmap.fillRectangle(int,int,int,int)"""
        super(__Pixmap, self).fillRectangle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def drawCircle(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawCircle(int,int,int)"""
        super(__Pixmap, self).drawCircle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def drawPixmap(self, arg0: 'Pixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixmap(com.badlogic.gdx.graphics.Pixmap,int,int,int,int,int,int)"""
        super(__Pixmap, self).drawPixmap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @overload
    def __init__(self, arg0: bytes, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.Pixmap(byte[],int,int)"""
        val = __Pixmap(bytes, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def drawPixmap(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawPixmap(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        super(__Pixmap, self).drawPixmap(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public com.badlogic.gdx.graphics.Pixmap(java.nio.ByteBuffer)"""
        val = __Pixmap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isDisposed(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Pixmap.isDisposed()"""
        return bool.__wrap(super(Pixmap, self).isDisposed())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFilter(self) -> 'Filter':
        """public com.badlogic.gdx.graphics.Pixmap$Filter com.badlogic.gdx.graphics.Pixmap.getFilter()"""
        return 'Filter'.__wrap(super(Pixmap, self).getFilter())

    @overload
    def drawLine(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Pixmap.drawLine(int,int,int,int)"""
        super(__Pixmap, self).drawLine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'Gdx2DPixmap'):
        """public com.badlogic.gdx.graphics.Pixmap(com.badlogic.gdx.graphics.g2d.Gdx2DPixmap)"""
        val = __Pixmap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def fillCircle(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Pixmap.fillCircle(int,int,int)"""
        super(__Pixmap, self).fillCircle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def setFilter(self, arg0: 'Filter'):
        """public void com.badlogic.gdx.graphics.Pixmap.setFilter(com.badlogic.gdx.graphics.Pixmap$Filter)"""
        super(__Pixmap, self).setFilter(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.Texture3D
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.Texture as __Texture_TextureFilter
__TextureFilter = __Texture_TextureFilter.TextureFilter
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.Texture3DData as __Texture3DData
__Texture3DData = __Texture3DData
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture_TextureWrap
__TextureWrap = __Texture_TextureWrap.TextureWrap
import com.badlogic.gdx.graphics.Texture3D as __Texture3D
__Texture3D = __Texture3D
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Texture3D(__GLTexture, GLTexture):
    """com.badlogic.gdx.graphics.Texture3D"""
 
    @staticmethod
    def __wrap(java_value: __Texture3D) -> 'Texture3D':
        return Texture3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Texture3D):
        """
        Dynamic initializer for Texture3D.
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
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getVWrap())

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1, __boolean.valueOf(arg2))

    @staticmethod
    @overload
    def invalidateAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture3D.invalidateAllTextureArrays(com.badlogic.gdx.Application)"""
        __Texture3D.invalidateAllTextureArrays(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public com.badlogic.gdx.graphics.Texture3D(int,int,int,int,int,int)"""
        val = __Texture3D(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Texture3D.isManaged()"""
        return bool.__wrap(super(Texture3D, self).isManaged())

    @overload
    def upload(self):
        """public void com.badlogic.gdx.graphics.Texture3D.upload()"""
        super(Texture3D, self).upload()

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1)

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(__GLTexture, self).bind(__int.valueOf(arg0))

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture3D.getWidth()"""
        return int.__wrap(super(Texture3D, self).getWidth())

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).setAnisotropicFilter(__float.valueOf(arg0)))

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMagFilter())

    @overload
    def getData(self) -> 'Texture3DData':
        """public com.badlogic.gdx.graphics.Texture3DData com.badlogic.gdx.graphics.Texture3D.getData()"""
        return 'Texture3DData'.__wrap(super(Texture3D, self).getData())

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Texture3D.getManagedStatus()"""
        return str.__wrap(__Texture3D.getManagedStatus())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture3D.getDepth()"""
        return int.__wrap(super(Texture3D, self).getDepth())

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Texture3DData'):
        """public com.badlogic.gdx.graphics.Texture3D(com.badlogic.gdx.graphics.Texture3DData)"""
        val = __Texture3D(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.GLTexture.dispose()"""
        super(GLTexture, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).setFilter(arg0, arg1)

    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: 'TextureWrap', arg3: bool):
        """public void com.badlogic.gdx.graphics.Texture3D.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(__Texture3D, self).unsafeSetWrap(arg0, arg1, arg2, __boolean.valueOf(arg3))

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float.__wrap(__GLTexture.getMaxAnisotropicFilterLevel())

    @staticmethod
    @overload
    def clearAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture3D.clearAllTextureArrays(com.badlogic.gdx.Application)"""
        __Texture3D.clearAllTextureArrays(arg0)

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).setWrap(arg0, arg1)

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        __GLTexture.uploadImageData(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.Texture3D.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__Texture3D, self).setWrap(arg0, arg1, arg2)

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getUWrap())

    @staticmethod
    @overload
    def getNumManagedTextures3D() -> int:
        """public static int com.badlogic.gdx.graphics.Texture3D.getNumManagedTextures3D()"""
        return int.__wrap(__Texture3D.getNumManagedTextures3D())

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMinFilter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float.__wrap(super(GLTexture, self).getAnisotropicFilter())

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.Texture3D.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__Texture3D, self).unsafeSetWrap(arg0, arg1, arg2)

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int.__wrap(super(GLTexture, self).getTextureObjectHandle())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture3D.getHeight()"""
        return int.__wrap(super(Texture3D, self).getHeight()) 
 
 
# CLASS: com.badlogic.gdx.graphics.PerspectiveCamera
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import com.badlogic.gdx.graphics.PerspectiveCamera as __PerspectiveCamera
__PerspectiveCamera = __PerspectiveCamera
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PerspectiveCamera(__Camera, Camera):
    """com.badlogic.gdx.graphics.PerspectiveCamera"""
 
    @staticmethod
    def __wrap(java_value: __PerspectiveCamera) -> 'PerspectiveCamera':
        return PerspectiveCamera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PerspectiveCamera):
        """
        Dynamic initializer for PerspectiveCamera.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.PerspectiveCamera()"""
        val = __PerspectiveCamera()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(__Camera, self).lookAt(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).project(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(__Camera, self).rotate(arg0, __float.valueOf(arg1))

    @override
    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(__Camera, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(__Camera, self).transform(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'.__wrap(super(__Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__Camera, self).rotate(arg0)

    @override
    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(__Camera, self).rotateAround(arg0, arg1, __float.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).unproject(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float):
        """public com.badlogic.gdx.graphics.PerspectiveCamera(float,float,float)"""
        val = __PerspectiveCamera(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).unproject(arg0))

    @override
    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(__Camera, self).lookAt(arg0)

    @override
    @overload
    def update(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update(boolean)"""
        super(__PerspectiveCamera, self).update(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(__Camera, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(Camera, self).normalizeUp()

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.PerspectiveCamera.update()"""
        super(PerspectiveCamera, self).update()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.PerspectiveCamera()"""
        val = __PerspectiveCamera()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(__Camera, self).rotate(arg0)

    @overload
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).project(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(__Camera, self).translate(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.GL20
import java.nio.IntBuffer as IntBuffer
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
import java.nio.Buffer as Buffer
from builtins import float
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
 
class GL20(ABC):
    """com.badlogic.gdx.graphics.GL20"""
 
    @staticmethod
    def __wrap(java_value: __GL20) -> 'GL20':
        return GL20(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL20):
        """
        Dynamic initializer for GL20.
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
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.GL32$DebugProc
import com.badlogic.gdx.graphics.GL32 as __GL32_DebugProc
__DebugProc = __GL32_DebugProc.DebugProc
from abc import abstractmethod, ABC
 
class DebugProc(ABC):
    """com.badlogic.gdx.graphics.GL32.DebugProc"""
 
    @staticmethod
    def __wrap(java_value: __DebugProc) -> 'DebugProc':
        return DebugProc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DebugProc):
        """
        Dynamic initializer for DebugProc.
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
    def onMessage(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str):
        """public abstract void com.badlogic.gdx.graphics.GL32$DebugProc.onMessage(int,int,int,int,java.lang.String)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureArrayData$Factory
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.TextureArrayData as __TextureArrayData_Factory
__Factory = __TextureArrayData_Factory.Factory
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.TextureArrayData as __TextureArrayData
__TextureArrayData = __TextureArrayData
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Factory():
    """com.badlogic.gdx.graphics.TextureArrayData.Factory"""
 
    @staticmethod
    def __wrap(java_value: __Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Factory):
        """
        Dynamic initializer for Factory.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def loadFromFiles(arg0: 'Format', arg1: bool, *arg2: 'files.FileHandle') -> 'TextureArrayData':
        """public static com.badlogic.gdx.graphics.TextureArrayData com.badlogic.gdx.graphics.TextureArrayData$Factory.loadFromFiles(com.badlogic.gdx.graphics.Pixmap$Format,boolean,com.badlogic.gdx.files.FileHandle...)"""
        return TextureArrayData.__wrap(__Factory.loadFromFiles(arg0, __boolean.valueOf(arg1), arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.TextureArrayData$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.TextureArrayData$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureData
import com.badlogic.gdx.graphics.TextureData as __TextureData
__TextureData = __TextureData
from abc import abstractmethod, ABC
 
class TextureData(ABC):
    """com.badlogic.gdx.graphics.TextureData"""
 
    @staticmethod
    def __wrap(java_value: __TextureData) -> 'TextureData':
        return TextureData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureData):
        """
        Dynamic initializer for TextureData.
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
    def getFormat(self, ):
        """public abstract com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.TextureData.getFormat()"""
        pass

    @abstractmethod
    def useMipMaps(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.useMipMaps()"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.TextureData.getType()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureData.getHeight()"""
        pass

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.isManaged()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.isPrepared()"""
        pass

    @abstractmethod
    def disposePixmap(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureData.disposePixmap()"""
        pass

    @abstractmethod
    def consumeCustomData(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.TextureData.consumeCustomData(int)"""
        pass

    @abstractmethod
    def consumePixmap(self, ):
        """public abstract com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.TextureData.consumePixmap()"""
        pass

    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.TextureData.prepare()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureData.getWidth()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.Texture$TextureWrap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture_TextureWrap
__TextureWrap = __Texture_TextureWrap.TextureWrap
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class TextureWrap(__Enum, Enum):
    """com.badlogic.gdx.graphics.Texture.TextureWrap"""
 
    @staticmethod
    def __wrap(java_value: __TextureWrap) -> 'TextureWrap':
        return TextureWrap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureWrap):
        """
        Dynamic initializer for TextureWrap.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextureWrap':
        """public static com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.Texture$TextureWrap.valueOf(java.lang.String)"""
        return TextureWrap.__wrap(__TextureWrap.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getGLEnum(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture$TextureWrap.getGLEnum()"""
        return int.__wrap(super(TextureWrap, self).getGLEnum())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['TextureWrap']:
        """public static com.badlogic.gdx.graphics.Texture$TextureWrap[] com.badlogic.gdx.graphics.Texture$TextureWrap.values()"""
        return List[TextureWrap].__wrap(__TextureWrap.values()) 
 
 
# CLASS: com.badlogic.gdx.graphics.VertexAttributes$Usage
from builtins import str
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes_Usage
__Usage = __VertexAttributes_Usage.Usage
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Usage():
    """com.badlogic.gdx.graphics.VertexAttributes.Usage"""
 
    @staticmethod
    def __wrap(java_value: __Usage) -> 'Usage':
        return Usage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Usage):
        """
        Dynamic initializer for Usage.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.VertexAttributes$Usage()"""
        val = __Usage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.VertexAttributes$Usage()"""
        val = __Usage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.GL32
from builtins import str
import com.badlogic.gdx.graphics.GL31 as __GL31
__GL31 = __GL31
import com.badlogic.gdx.graphics.GL30 as __GL30
__GL30 = __GL30
import com.badlogic.gdx.graphics.GL32 as __GL32
__GL32 = __GL32
import java.nio.IntBuffer as IntBuffer
from builtins import float
import java.nio.LongBuffer as LongBuffer
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
import java.nio.Buffer as Buffer
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class GL32(ABC, __GL31, GL31):
    """com.badlogic.gdx.graphics.GL32"""
 
    @staticmethod
    def __wrap(java_value: __GL32) -> 'GL32':
        return GL32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL32):
        """
        Dynamic initializer for GL32.
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
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawElementsInstanced(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glFramebufferParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glFramebufferParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindTransformFeedback(int,int)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glResumeTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glResumeTransformFeedback()"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glGetPointerv(self, arg0: int):
        """public abstract long com.badlogic.gdx.graphics.GL32.glGetPointerv(int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glProgramUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glProgramUniform2ui(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2ui(int,int,int,int)"""
        pass

    @abstractmethod
    def glPopDebugGroup(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL32.glPopDebugGroup()"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glMinSampleShading(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL32.glMinSampleShading(float)"""
        pass

    @abstractmethod
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsTransformFeedback(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsTransformFeedback(int)"""
        pass

    @abstractmethod
    def glDrawElementsIndirect(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawElementsIndirect(int,int,long)"""
        pass

    @abstractmethod
    def glProgramUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawArraysInstanced(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformBlockBinding(int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1i(int,int,int)"""
        pass

    @abstractmethod
    def glBeginTransformFeedback(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginTransformFeedback(int)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparatei(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendFuncSeparatei(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetBooleani_v(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetBooleani_v(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetnUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetnUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glTexBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawElementsInstancedBaseVertex(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBindVertexArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindVertexArray(int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glEndQuery(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndQuery(int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glBindSampler(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindSampler(int,int)"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4f(int,int,float,float,float,float)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3f(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3f(int,int,float,float,float)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glMapBufferRange(int,int,int,int)"""
        pass

    @abstractmethod
    def glBindProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGetMultisamplefv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetMultisamplefv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBlendFunci(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendFunci(int,int,int)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfi(int,int,float,int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glPushDebugGroup(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL32.glPushDebugGroup(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glProgramParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDebugMessageControl(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: bool):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDebugMessageControl(int,int,int,java.nio.IntBuffer,boolean)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glGetnUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetnUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glBindVertexBuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindVertexBuffer(int,int,long,int)"""
        pass

    @abstractmethod
    def glDrawArraysIndirect(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDrawArraysIndirect(int,long)"""
        pass

    @abstractmethod
    def glSampleMaski(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glSampleMaski(int,int)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glIsSampler(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsSampler(int)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform2uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUnmapBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glUnmapBuffer(int)"""
        pass

    @abstractmethod
    def glDrawRangeElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer', arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawRangeElementsBaseVertex(int,int,int,int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glDebugMessageInsert(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: str):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDebugMessageInsert(int,int,int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glDispatchComputeIndirect(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchComputeIndirect(long)"""
        pass

    @abstractmethod
    def glVertexAttribFormat(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribFormat(int,int,int,boolean,int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glBlendEquationi(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendEquationi(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glProgramUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glObjectLabel(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL32.glObjectLabel(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGenProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGenProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindImageTexture(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glBindImageTexture(int,int,int,boolean,int,int,int)"""
        pass

    @abstractmethod
    def glReadBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glReadBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetTexLevelParameterfv(self, arg0: int, arg1: int, arg2: int, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameterfv(int,int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsQuery(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsQuery(int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glProgramUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glIsEnabledi(self, arg0: int, arg1: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL32.glIsEnabledi(int,int)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform2i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2i(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexStorage2DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool):
        """public abstract void com.badlogic.gdx.graphics.GL31.glTexStorage2DMultisample(int,int,int,int,int,boolean)"""
        pass

    @abstractmethod
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glEnablei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glEnablei(int,int)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetProgramResourceName(self, arg0: int, arg1: int, arg2: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramResourceName(int,int,int)"""
        pass

    @abstractmethod
    def glTexStorage3DMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexStorage3DMultisample(int,int,int,int,int,int,boolean)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetnUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetnUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramPipelineiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramPipelineiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glGetProgramResourceIndex(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceIndex(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glProgramUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformBlockIndex(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetUniformBlockIndex(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetProgramResourceLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract int com.badlogic.gdx.graphics.GL31.glGetProgramResourceLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glDebugMessageCallback(self, arg0: 'DebugProc'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDebugMessageCallback(com.badlogic.gdx.graphics.GL32$DebugProc)"""
        pass

    @abstractmethod
    def glGetFramebufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetFramebufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform3ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDrawElementsInstancedBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawElementsInstancedBaseVertex(int,int,int,java.nio.Buffer,int,int)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glPatchParameteri(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glPatchParameteri(int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribIPointer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendEquationSeparatei(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendEquationSeparatei(int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBeginQuery(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginQuery(int,int)"""
        pass

    @abstractmethod
    def glGetObjectLabel(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL32.glGetObjectLabel(int,int)"""
        pass

    @abstractmethod
    def glGetTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform1f(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1f(int,int,float)"""
        pass

    @abstractmethod
    def glProgramUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4i(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramPipelineInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL31.glGetProgramPipelineInfoLog(int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexBuffer(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexBuffer(int,int,int)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramInterfaceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramInterfaceiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        pass

    @abstractmethod
    def glActiveShaderProgram(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glActiveShaderProgram(int,int)"""
        pass

    @abstractmethod
    def glProgramUniform4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4ui(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisablei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDisablei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsProgramPipeline(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL31.glIsProgramPipeline(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glGetDebugMessageLog(self, arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer', arg6: 'ByteBuffer'):
        """public abstract int com.badlogic.gdx.graphics.GL32.glGetDebugMessageLog(int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.ByteBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetInteger64v(int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetStringi(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetStringi(int,int)"""
        pass

    @abstractmethod
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyBufferSubData(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glEndTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndTransformFeedback()"""
        pass

    @abstractmethod
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glGetTexParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetTexLevelParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetTexLevelParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetFragDataLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetFragDataLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glReadnPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glReadnPixels(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glProgramUniform2f(self, arg0: int, arg1: int, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform2f(int,int,float,float)"""
        pass

    @abstractmethod
    def glUseProgramStages(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glUseProgramStages(int,int,int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribBinding(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribBinding(int,int)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsVertexArray(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsVertexArray(int)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glProgramUniform1ui(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1ui(int,int,int)"""
        pass

    @abstractmethod
    def glVertexBindingDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexBindingDivisor(int,int)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glCreateShaderProgramv(self, arg0: int, arg1: 'String'):
        """public abstract int com.badlogic.gdx.graphics.GL31.glCreateShaderProgramv(int,java.lang.String[])"""
        pass

    @abstractmethod
    def glGetProgramResourceiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer', arg4: 'IntBuffer', arg5: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glGetProgramResourceiv(int,int,int,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glProgramUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glSamplerParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glSamplerParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glProgramUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glBlendBarrier(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL32.glBlendBarrier()"""
        pass

    @abstractmethod
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDispatchCompute(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDispatchCompute(int,int,int)"""
        pass

    @abstractmethod
    def glPauseTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glPauseTransformFeedback()"""
        pass

    @abstractmethod
    def glMemoryBarrier(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrier(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawElementsBaseVertex(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glDrawElementsBaseVertex(int,int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glColorMaski(self, arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool):
        """public abstract void com.badlogic.gdx.graphics.GL32.glColorMaski(int,boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glMemoryBarrierByRegion(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glMemoryBarrierByRegion(int)"""
        pass

    @abstractmethod
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFlushMappedBufferRange(int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glGetGraphicsResetStatus(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL32.glGetGraphicsResetStatus()"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCopyImageSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glCopyImageSubData(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glValidateProgramPipeline(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glValidateProgramPipeline(int)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glProgramUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glProgramUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferBase(int,int,int)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glSamplerParameterIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTexture(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL32.glFramebufferTexture(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFramebufferTextureLayer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribDivisor(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribIFormat(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL31.glVertexAttribIFormat(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetBufferPointerv(self, arg0: int, arg1: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glGetBufferPointerv(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgramPipelines(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL31.glDeleteProgramPipelines(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL32.glTexParameterIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass

    @abstractmethod
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteri(int,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.Texture$TextureFilter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.graphics.Texture as __Texture_TextureFilter
__TextureFilter = __Texture_TextureFilter.TextureFilter
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import int
 
class TextureFilter(__Enum, Enum):
    """com.badlogic.gdx.graphics.Texture.TextureFilter"""
 
    @staticmethod
    def __wrap(java_value: __TextureFilter) -> 'TextureFilter':
        return TextureFilter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureFilter):
        """
        Dynamic initializer for TextureFilter.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def values() -> List['TextureFilter']:
        """public static com.badlogic.gdx.graphics.Texture$TextureFilter[] com.badlogic.gdx.graphics.Texture$TextureFilter.values()"""
        return List[TextureFilter].__wrap(__TextureFilter.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getGLEnum(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture$TextureFilter.getGLEnum()"""
        return int.__wrap(super(TextureFilter, self).getGLEnum())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isMipMap(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Texture$TextureFilter.isMipMap()"""
        return bool.__wrap(super(TextureFilter, self).isMipMap())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextureFilter':
        """public static com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.Texture$TextureFilter.valueOf(java.lang.String)"""
        return TextureFilter.__wrap(__TextureFilter.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.OrthographicCamera
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.OrthographicCamera as __OrthographicCamera
__OrthographicCamera = __OrthographicCamera
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OrthographicCamera(__Camera, Camera):
    """com.badlogic.gdx.graphics.OrthographicCamera"""
 
    @staticmethod
    def __wrap(java_value: __OrthographicCamera) -> 'OrthographicCamera':
        return OrthographicCamera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrthographicCamera):
        """
        Dynamic initializer for OrthographicCamera.
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
    def translate(self, arg0: 'Vector2'):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.translate(com.badlogic.gdx.math.Vector2)"""
        super(__OrthographicCamera, self).translate(arg0)

    @override
    @overload
    def update(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.update(boolean)"""
        super(__OrthographicCamera, self).update(__boolean.valueOf(arg0))

    @override
    @overload
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(__Camera, self).lookAt(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).project(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(__Camera, self).rotate(arg0, __float.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.OrthographicCamera()"""
        val = __OrthographicCamera()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(__Camera, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(__Camera, self).transform(arg0)

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'.__wrap(super(__Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.translate(float,float)"""
        super(__OrthographicCamera, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__Camera, self).rotate(arg0)

    @override
    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(__Camera, self).rotateAround(arg0, arg1, __float.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).unproject(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).unproject(arg0))

    @override
    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(__Camera, self).lookAt(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(__Camera, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(Camera, self).normalizeUp()

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

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
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(__Camera, self).rotate(arg0)

    @overload
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).project(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.OrthographicCamera()"""
        val = __OrthographicCamera()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public com.badlogic.gdx.graphics.OrthographicCamera(float,float)"""
        val = __OrthographicCamera(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.rotate(float)"""
        super(__OrthographicCamera, self).rotate(__float.valueOf(arg0))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.update()"""
        super(OrthographicCamera, self).update()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setToOrtho(self, arg0: bool, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.setToOrtho(boolean,float,float)"""
        super(__OrthographicCamera, self).setToOrtho(__boolean.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(__Camera, self).translate(arg0)

    @overload
    def setToOrtho(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.OrthographicCamera.setToOrtho(boolean)"""
        super(__OrthographicCamera, self).setToOrtho(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.Cursor$SystemCursor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.Cursor as __Cursor_SystemCursor
__SystemCursor = __Cursor_SystemCursor.SystemCursor
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class SystemCursor(__Enum, Enum):
    """com.badlogic.gdx.graphics.Cursor.SystemCursor"""
 
    @staticmethod
    def __wrap(java_value: __SystemCursor) -> 'SystemCursor':
        return SystemCursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SystemCursor):
        """
        Dynamic initializer for SystemCursor.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'SystemCursor':
        """public static com.badlogic.gdx.graphics.Cursor$SystemCursor com.badlogic.gdx.graphics.Cursor$SystemCursor.valueOf(java.lang.String)"""
        return SystemCursor.__wrap(__SystemCursor.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def values() -> List['SystemCursor']:
        """public static com.badlogic.gdx.graphics.Cursor$SystemCursor[] com.badlogic.gdx.graphics.Cursor$SystemCursor.values()"""
        return List[SystemCursor].__wrap(__SystemCursor.values())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.graphics.PixmapIO
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.graphics.PixmapIO as __PixmapIO
__PixmapIO = __PixmapIO
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PixmapIO():
    """com.badlogic.gdx.graphics.PixmapIO"""
 
    @staticmethod
    def __wrap(java_value: __PixmapIO) -> 'PixmapIO':
        return PixmapIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PixmapIO):
        """
        Dynamic initializer for PixmapIO.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.PixmapIO()"""
        val = __PixmapIO()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def writePNG(arg0: 'FileHandle', arg1: 'Pixmap', arg2: int, arg3: bool):
        """public static void com.badlogic.gdx.graphics.PixmapIO.writePNG(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap,int,boolean)"""
        __PixmapIO.writePNG(arg0, arg1, __int.valueOf(arg2), __boolean.valueOf(arg3))

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
    def readCIM(arg0: 'FileHandle') -> 'Pixmap':
        """public static com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.PixmapIO.readCIM(com.badlogic.gdx.files.FileHandle)"""
        return Pixmap.__wrap(__PixmapIO.readCIM(arg0))

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
    def writeCIM(arg0: 'FileHandle', arg1: 'Pixmap'):
        """public static void com.badlogic.gdx.graphics.PixmapIO.writeCIM(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap)"""
        __PixmapIO.writeCIM(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.PixmapIO()"""
        val = __PixmapIO()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def writePNG(arg0: 'FileHandle', arg1: 'Pixmap'):
        """public static void com.badlogic.gdx.graphics.PixmapIO.writePNG(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap)"""
        __PixmapIO.writePNG(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.Camera
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Camera(ABC):
    """com.badlogic.gdx.graphics.Camera"""
 
    @staticmethod
    def __wrap(java_value: __Camera) -> 'Camera':
        return Camera(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Camera):
        """
        Dynamic initializer for Camera.
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

    @abstractmethod
    def update(self, ):
        """public abstract void com.badlogic.gdx.graphics.Camera.update()"""
        pass

    @abstractmethod
    def update(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.Camera.update(boolean)"""
        pass

    @overload
    def rotateAround(self, arg0: 'Vector3', arg1: 'Vector3', arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.rotateAround(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        super(__Camera, self).rotateAround(arg0, arg1, __float.valueOf(arg2))

    @overload
    def project(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).project(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.Camera()"""
        val = __Camera()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__Camera, self).rotate(arg0)

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(__Camera, self).rotate(arg0, __float.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def rotate(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.Camera.rotate(float,float,float,float)"""
        super(__Camera, self).rotate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def lookAt(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(float,float,float)"""
        super(__Camera, self).lookAt(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Camera.translate(float,float,float)"""
        super(__Camera, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def getPickRay(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float,float,float,float,float)"""
        return 'collision.Ray'.__wrap(super(__Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

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

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.translate(com.badlogic.gdx.math.Vector3)"""
        super(__Camera, self).translate(arg0)

    @overload
    def unproject(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).unproject(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def unproject(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.unproject(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).unproject(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getPickRay(self, arg0: float, arg1: float) -> 'collision.Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.graphics.Camera.getPickRay(float,float)"""
        return 'collision.Ray'.__wrap(super(__Camera, self).getPickRay(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def lookAt(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.Camera.lookAt(com.badlogic.gdx.math.Vector3)"""
        super(__Camera, self).lookAt(arg0)

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
    def project(self, arg0: 'Vector3', arg1: float, arg2: float, arg3: float, arg4: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Camera.project(com.badlogic.gdx.math.Vector3,float,float,float,float)"""
        return 'math.Vector3'.__wrap(super(__Camera, self).project(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.transform(com.badlogic.gdx.math.Matrix4)"""
        super(__Camera, self).transform(arg0)

    @overload
    def rotate(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Camera.rotate(com.badlogic.gdx.math.Matrix4)"""
        super(__Camera, self).rotate(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.Camera()"""
        val = __Camera()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def normalizeUp(self):
        """public void com.badlogic.gdx.graphics.Camera.normalizeUp()"""
        super(Camera, self).normalizeUp() 
 
 
# CLASS: com.badlogic.gdx.graphics.CubemapData
import com.badlogic.gdx.graphics.CubemapData as __CubemapData
__CubemapData = __CubemapData
from abc import abstractmethod, ABC
 
class CubemapData(ABC):
    """com.badlogic.gdx.graphics.CubemapData"""
 
    @staticmethod
    def __wrap(java_value: __CubemapData) -> 'CubemapData':
        return CubemapData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CubemapData):
        """
        Dynamic initializer for CubemapData.
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
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.CubemapData.isManaged()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.CubemapData.isPrepared()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.CubemapData.getHeight()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.CubemapData.getWidth()"""
        pass

    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.CubemapData.prepare()"""
        pass

    @abstractmethod
    def consumeCubemapData(self, ):
        """public abstract void com.badlogic.gdx.graphics.CubemapData.consumeCubemapData()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.GL30
from builtins import str
import com.badlogic.gdx.graphics.GL30 as __GL30
__GL30 = __GL30
import java.nio.IntBuffer as IntBuffer
import java.nio.Buffer as Buffer
import com.badlogic.gdx.graphics.GL20 as __GL20
__GL20 = __GL20
from builtins import float
import java.nio.LongBuffer as LongBuffer
from abc import abstractmethod, ABC
import java.nio.FloatBuffer as FloatBuffer
from builtins import int
 
class GL30(ABC, __GL20, GL20):
    """com.badlogic.gdx.graphics.GL30"""
 
    @staticmethod
    def __wrap(java_value: __GL30) -> 'GL30':
        return GL30(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GL30):
        """
        Dynamic initializer for GL30.
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
    def glDrawElementsInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawElementsInstanced(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glIsRenderbuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsRenderbuffer(int)"""
        pass

    @abstractmethod
    def glCreateShader(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateShader(int)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int,java.nio.Buffer,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glBindTransformFeedback(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindTransformFeedback(int,int)"""
        pass

    @abstractmethod
    def glGetActiveAttrib(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveAttrib(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribI4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glGetUniformuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glResumeTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glResumeTransformFeedback()"""
        pass

    @abstractmethod
    def glUniform4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glBindFramebuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindFramebuffer(int,int)"""
        pass

    @abstractmethod
    def glDisable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisable(int)"""
        pass

    @abstractmethod
    def glBlendColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glGenBuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenBuffer()"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glBlendEquationSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquationSeparate(int,int)"""
        pass

    @abstractmethod
    def glDeleteProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteProgram(int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glRenderbufferStorageMultisample(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glRenderbufferStorageMultisample(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glCullFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCullFace(int)"""
        pass

    @abstractmethod
    def glLineWidth(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLineWidth(float)"""
        pass

    @abstractmethod
    def glVertexAttrib3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glCompressedTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexImage2D(int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMask(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMask(int)"""
        pass

    @abstractmethod
    def glUniform2iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix3x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockiv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockiv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDepthRangef(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthRangef(float,float)"""
        pass

    @abstractmethod
    def glUniform1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1f(int,float)"""
        pass

    @abstractmethod
    def glGetError(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetError()"""
        pass

    @abstractmethod
    def glVertexAttrib1f(self, arg0: int, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1f(int,float)"""
        pass

    @abstractmethod
    def glUniformMatrix4x2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlitFramebuffer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBlitFramebuffer(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glClearBufferuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetBufferParameteri64v(self, arg0: int, arg1: int, arg2: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetBufferParameteri64v(int,int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glDetachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDetachShader(int,int)"""
        pass

    @abstractmethod
    def glClearColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearColor(float,float,float,float)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsTransformFeedback(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsTransformFeedback(int)"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glGetUniformfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDrawArraysInstanced(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawArraysInstanced(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformBlockBinding(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformBlockBinding(int,int,int)"""
        pass

    @abstractmethod
    def glDeleteBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffer(int)"""
        pass

    @abstractmethod
    def glBeginTransformFeedback(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginTransformFeedback(int)"""
        pass

    @abstractmethod
    def glGetAttribLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetAttribLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib3fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib3fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glBindVertexArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindVertexArray(int)"""
        pass

    @abstractmethod
    def glUniform1i(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1i(int,int)"""
        pass

    @abstractmethod
    def glUniform3uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform3uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearStencil(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearStencil(int)"""
        pass

    @abstractmethod
    def glGetShaderInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetShaderInfoLog(int)"""
        pass

    @abstractmethod
    def glEndQuery(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndQuery(int)"""
        pass

    @abstractmethod
    def glIsShader(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsShader(int)"""
        pass

    @abstractmethod
    def glUniform1iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage3D(int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffer(int)"""
        pass

    @abstractmethod
    def glGenFramebuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenFramebuffer()"""
        pass

    @abstractmethod
    def glBindSampler(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindSampler(int,int)"""
        pass

    @abstractmethod
    def glUseProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUseProgram(int)"""
        pass

    @abstractmethod
    def glFinish(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFinish()"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferRange(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glReleaseShaderCompiler(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReleaseShaderCompiler()"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetActiveUniformBlockName(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetActiveUniformBlockName(int,int)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glClearDepthf(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClearDepthf(float)"""
        pass

    @abstractmethod
    def glStencilOp(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOp(int,int,int)"""
        pass

    @abstractmethod
    def glMapBufferRange(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glMapBufferRange(int,int,int,int)"""
        pass

    @abstractmethod
    def glBlendEquation(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendEquation(int)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,int[],int)"""
        pass

    @abstractmethod
    def glCheckFramebufferStatus(self, arg0: int):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCheckFramebufferStatus(int)"""
        pass

    @abstractmethod
    def glBindTexture(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindTexture(int,int)"""
        pass

    @abstractmethod
    def glGetBufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetRenderbufferParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetRenderbufferParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glClearBufferfi(self, arg0: int, arg1: int, arg2: float, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfi(int,int,float,int)"""
        pass

    @abstractmethod
    def glShaderSource(self, arg0: int, arg1: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderSource(int,java.lang.String)"""
        pass

    @abstractmethod
    def glClearBufferfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetUniformLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGetUniformLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGetUniformiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetUniformiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPolygonOffset(self, arg0: float, arg1: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPolygonOffset(float,float)"""
        pass

    @abstractmethod
    def glProgramParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glProgramParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glGetBooleanv(self, arg0: int, arg1: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetBooleanv(int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glStencilMaskSeparate(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilMaskSeparate(int,int)"""
        pass

    @abstractmethod
    def glCreateProgram(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glCreateProgram()"""
        pass

    @abstractmethod
    def glUniformMatrix2fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix2fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glHint(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glHint(int,int)"""
        pass

    @abstractmethod
    def glDeleteSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glGenFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffer(int)"""
        pass

    @abstractmethod
    def glIsSampler(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsSampler(int)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,int[],int)"""
        pass

    @abstractmethod
    def glBindBuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindBuffer(int,int)"""
        pass

    @abstractmethod
    def glGenTextures(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenTextures(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUnmapBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glUnmapBuffer(int)"""
        pass

    @abstractmethod
    def glGenVertexArrays(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenVertexArrays(int,int[],int)"""
        pass

    @abstractmethod
    def glViewport(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glViewport(int,int,int,int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetVertexAttribIuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGenTransformFeedbacks(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenTransformFeedbacks(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform1fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform1fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glFlush(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFlush()"""
        pass

    @abstractmethod
    def glClear(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glClear(int)"""
        pass

    @abstractmethod
    def glActiveTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glActiveTexture(int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyTexSubImage3D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glAttachShader(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glAttachShader(int,int)"""
        pass

    @abstractmethod
    def glIsTexture(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsTexture(int)"""
        pass

    @abstractmethod
    def glVertexAttrib4fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTransformFeedbackVaryings(self, arg0: int, arg1: 'String', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTransformFeedbackVaryings(int,java.lang.String[],int)"""
        pass

    @abstractmethod
    def glUniformMatrix4x3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix4x3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glReadBuffer(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glReadBuffer(int)"""
        pass

    @abstractmethod
    def glFramebufferTexture2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferTexture2D(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGenerateMipmap(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenerateMipmap(int)"""
        pass

    @abstractmethod
    def glGetVertexAttribIiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetVertexAttribIiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform3f(self, arg0: int, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3f(int,float,float,float)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribPointer(int,int,int,boolean,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteFramebuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteFramebuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsQuery(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsQuery(int)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'int', arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,int[],int)"""
        pass

    @abstractmethod
    def glDrawRangeElements(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawRangeElements(int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glVertexAttrib1fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib1fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glCompressedTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompressedTexSubImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glValidateProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glValidateProgram(int)"""
        pass

    @abstractmethod
    def glTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetProgramInfoLog(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetProgramInfoLog(int)"""
        pass

    @abstractmethod
    def glGetFloatv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFloatv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glStencilOpSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilOpSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glStencilFunc(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFunc(int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribPointerv(self, arg0: int, arg1: int, arg2: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribPointerv(int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glColorMask(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glColorMask(boolean,boolean,boolean,boolean)"""
        pass

    @abstractmethod
    def glBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferSubData(int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glDeleteShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteShader(int)"""
        pass

    @abstractmethod
    def glRenderbufferStorage(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glRenderbufferStorage(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetShaderPrecisionFormat(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderPrecisionFormat(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2fv(self, arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2fv(int,int,float[],int)"""
        pass

    @abstractmethod
    def glScissor(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glScissor(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetUniformIndices(self, arg0: int, arg1: 'String', arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetUniformIndices(int,java.lang.String[],java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttrib2fv(self, arg0: int, arg1: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2fv(int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsProgram(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsProgram(int)"""
        pass

    @abstractmethod
    def glGetUniformBlockIndex(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetUniformBlockIndex(int,java.lang.String)"""
        pass

    @abstractmethod
    def glStencilFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glStencilFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2f(int,float,float)"""
        pass

    @abstractmethod
    def glUniform3i(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3i(int,int,int,int)"""
        pass

    @abstractmethod
    def glUniform1uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform1uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4uiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniform4uiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteVertexArrays(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteVertexArrays(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glReadPixels(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glReadPixels(int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glUniform4fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFuncSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFuncSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glShaderBinary(self, arg0: int, arg1: 'IntBuffer', arg2: int, arg3: 'Buffer', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glShaderBinary(int,java.nio.IntBuffer,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glSamplerParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glVertexAttribIPointer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribIPointer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix2x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix2x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetFramebufferAttachmentParameteriv(self, arg0: int, arg1: int, arg2: int, arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetFramebufferAttachmentParameteriv(int,int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glCopyTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glEnable(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnable(int)"""
        pass

    @abstractmethod
    def glTexSubImage3D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexSubImage3D(int,int,int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib4f(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib4f(int,float,float,float,float)"""
        pass

    @abstractmethod
    def glGetActiveUniformsiv(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetActiveUniformsiv(int,int,java.nio.IntBuffer,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBeginQuery(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBeginQuery(int,int)"""
        pass

    @abstractmethod
    def glGetShaderiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetShaderiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glLinkProgram(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glLinkProgram(int)"""
        pass

    @abstractmethod
    def glUniform2i(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform2i(int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix3fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix3fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetIntegerv(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetIntegerv(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPixelStorei(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glPixelStorei(int,int)"""
        pass

    @abstractmethod
    def glVertexAttrib2f(self, arg0: int, arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttrib2f(int,float,float)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glTexImage2D(int,int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateSubFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateSubFramebuffer(int,int,java.nio.IntBuffer,int,int,int,int)"""
        pass

    @abstractmethod
    def glVertexAttribI4ui(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribI4ui(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGenRenderbuffer(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenRenderbuffer()"""
        pass

    @abstractmethod
    def glUniformMatrix3x4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glUniformMatrix3x4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetInteger64v(self, arg0: int, arg1: 'LongBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetInteger64v(int,java.nio.LongBuffer)"""
        pass

    @abstractmethod
    def glSampleCoverage(self, arg0: float, arg1: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glSampleCoverage(float,boolean)"""
        pass

    @abstractmethod
    def glCompileShader(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCompileShader(int)"""
        pass

    @abstractmethod
    def glGetAttachedShaders(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetAttachedShaders(int,int,java.nio.Buffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetStringi(self, arg0: int, arg1: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL30.glGetStringi(int,int)"""
        pass

    @abstractmethod
    def glCopyBufferSubData(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glCopyBufferSubData(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,float[],int)"""
        pass

    @abstractmethod
    def glEndTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glEndTransformFeedback()"""
        pass

    @abstractmethod
    def glDrawBuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDrawBuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetFragDataLocation(self, arg0: int, arg1: str):
        """public abstract int com.badlogic.gdx.graphics.GL30.glGetFragDataLocation(int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenTexture(self, ):
        """public abstract int com.badlogic.gdx.graphics.GL20.glGenTexture()"""
        pass

    @abstractmethod
    def glIsBuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsBuffer(int)"""
        pass

    @abstractmethod
    def glTexParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteri(int,int,int)"""
        pass

    @abstractmethod
    def glDrawArrays(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawArrays(int,int,int)"""
        pass

    @abstractmethod
    def glDrawElements(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDrawElements(int,int,int,int)"""
        pass

    @abstractmethod
    def glGenQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetProgramiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetProgramiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glIsVertexArray(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL30.glIsVertexArray(int)"""
        pass

    @abstractmethod
    def glDepthFunc(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthFunc(int)"""
        pass

    @abstractmethod
    def glGetActiveUniform(self, arg0: int, arg1: int, arg2: 'IntBuffer', arg3: 'IntBuffer'):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetActiveUniform(int,int,java.nio.IntBuffer,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribPointer(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glVertexAttribPointer(int,int,int,boolean,int,int)"""
        pass

    @abstractmethod
    def glTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glUniform4iv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4iv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetString(self, arg0: int):
        """public abstract java.lang.String com.badlogic.gdx.graphics.GL20.glGetString(int)"""
        pass

    @abstractmethod
    def glDeleteRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glDeleteTexture(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDeleteTexture(int)"""
        pass

    @abstractmethod
    def glUniform3iv(self, arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3iv(int,int,int[],int)"""
        pass

    @abstractmethod
    def glDepthMask(self, arg0: bool):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDepthMask(boolean)"""
        pass

    @abstractmethod
    def glUniform4i(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform4i(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glBufferData(self, arg0: int, arg1: int, arg2: 'Buffer', arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBufferData(int,int,java.nio.Buffer,int)"""
        pass

    @abstractmethod
    def glClearBufferiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glClearBufferiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glPauseTransformFeedback(self, ):
        """public abstract void com.badlogic.gdx.graphics.GL30.glPauseTransformFeedback()"""
        pass

    @abstractmethod
    def glGetVertexAttribiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferRenderbuffer(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFramebufferRenderbuffer(int,int,int,int)"""
        pass

    @abstractmethod
    def glGetQueryObjectuiv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetQueryObjectuiv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glIsEnabled(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsEnabled(int)"""
        pass

    @abstractmethod
    def glGenRenderbuffers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGenRenderbuffers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFlushMappedBufferRange(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFlushMappedBufferRange(int,int,int)"""
        pass

    @abstractmethod
    def glInvalidateFramebuffer(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glInvalidateFramebuffer(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glBindRenderbuffer(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindRenderbuffer(int,int)"""
        pass

    @abstractmethod
    def glEnableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glEnableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glIsFramebuffer(self, arg0: int):
        """public abstract boolean com.badlogic.gdx.graphics.GL20.glIsFramebuffer(int)"""
        pass

    @abstractmethod
    def glUniformMatrix4fv(self, arg0: int, arg1: int, arg2: bool, arg3: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniformMatrix4fv(int,int,boolean,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBlendFunc(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBlendFunc(int,int)"""
        pass

    @abstractmethod
    def glUniform3fv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glUniform3fv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glBindBufferBase(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glBindBufferBase(int,int,int)"""
        pass

    @abstractmethod
    def glTexImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'Buffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexImage2D(int,int,int,int,int,int,int,int,java.nio.Buffer)"""
        pass

    @abstractmethod
    def glGetTexParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetTexParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glGetSamplerParameteriv(self, arg0: int, arg1: int, arg2: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGetSamplerParameteriv(int,int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glTexParameterf(self, arg0: int, arg1: int, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterf(int,int,float)"""
        pass

    @abstractmethod
    def glBindAttribLocation(self, arg0: int, arg1: int, arg2: str):
        """public abstract void com.badlogic.gdx.graphics.GL20.glBindAttribLocation(int,int,java.lang.String)"""
        pass

    @abstractmethod
    def glGenSamplers(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glGenSamplers(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glFramebufferTextureLayer(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glFramebufferTextureLayer(int,int,int,int,int)"""
        pass

    @abstractmethod
    def glDisableVertexAttribArray(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glDisableVertexAttribArray(int)"""
        pass

    @abstractmethod
    def glTexParameterfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glTexParameterfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glDeleteQueries(self, arg0: int, arg1: 'IntBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL30.glDeleteQueries(int,java.nio.IntBuffer)"""
        pass

    @abstractmethod
    def glVertexAttribDivisor(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glVertexAttribDivisor(int,int)"""
        pass

    @abstractmethod
    def glCopyTexSubImage2D(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glCopyTexSubImage2D(int,int,int,int,int,int,int,int)"""
        pass

    @abstractmethod
    def glGetVertexAttribfv(self, arg0: int, arg1: int, arg2: 'FloatBuffer'):
        """public abstract void com.badlogic.gdx.graphics.GL20.glGetVertexAttribfv(int,int,java.nio.FloatBuffer)"""
        pass

    @abstractmethod
    def glGetBufferPointerv(self, arg0: int, arg1: int):
        """public abstract java.nio.Buffer com.badlogic.gdx.graphics.GL30.glGetBufferPointerv(int,int)"""
        pass

    @abstractmethod
    def glFrontFace(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.GL20.glFrontFace(int)"""
        pass

    @abstractmethod
    def glSamplerParameteri(self, arg0: int, arg1: int, arg2: int):
        """public abstract void com.badlogic.gdx.graphics.GL30.glSamplerParameteri(int,int,int)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$Format
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Format(__Enum, Enum):
    """com.badlogic.gdx.graphics.Pixmap.Format"""
 
    @staticmethod
    def __wrap(java_value: __Format) -> 'Format':
        return Format(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Format):
        """
        Dynamic initializer for Format.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def toGlType(arg0: 'Format') -> int:
        """public static int com.badlogic.gdx.graphics.Pixmap$Format.toGlType(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return int.__wrap(__Format.toGlType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Format':
        """public static com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.Pixmap$Format.valueOf(java.lang.String)"""
        return Format.__wrap(__Format.valueOf(arg0))

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def toGlFormat(arg0: 'Format') -> int:
        """public static int com.badlogic.gdx.graphics.Pixmap$Format.toGlFormat(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return int.__wrap(__Format.toGlFormat(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def toGdx2DPixmapFormat(arg0: 'Format') -> int:
        """public static int com.badlogic.gdx.graphics.Pixmap$Format.toGdx2DPixmapFormat(com.badlogic.gdx.graphics.Pixmap$Format)"""
        return int.__wrap(__Format.toGdx2DPixmapFormat(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def fromGdx2DPixmapFormat(arg0: int) -> 'Format':
        """public static com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.Pixmap$Format.fromGdx2DPixmapFormat(int)"""
        return Format.__wrap(__Format.fromGdx2DPixmapFormat(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def values() -> List['Format']:
        """public static com.badlogic.gdx.graphics.Pixmap$Format[] com.badlogic.gdx.graphics.Pixmap$Format.values()"""
        return List[Format].__wrap(__Format.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Texture3DData
import com.badlogic.gdx.graphics.Texture3DData as __Texture3DData
__Texture3DData = __Texture3DData
from abc import abstractmethod, ABC
 
class Texture3DData(ABC):
    """com.badlogic.gdx.graphics.Texture3DData"""
 
    @staticmethod
    def __wrap(java_value: __Texture3DData) -> 'Texture3DData':
        return Texture3DData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Texture3DData):
        """
        Dynamic initializer for Texture3DData.
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
    def useMipMaps(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.Texture3DData.useMipMaps()"""
        pass

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.Texture3DData.isManaged()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getWidth()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.Texture3DData.isPrepared()"""
        pass

    @abstractmethod
    def getGLType(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getGLType()"""
        pass

    @abstractmethod
    def consume3DData(self, ):
        """public abstract void com.badlogic.gdx.graphics.Texture3DData.consume3DData()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getHeight()"""
        pass

    @abstractmethod
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.Texture3DData.prepare()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getDepth()"""
        pass

    @abstractmethod
    def getInternalFormat(self, ):
        """public abstract int com.badlogic.gdx.graphics.Texture3DData.getInternalFormat()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.PixmapIO$PNG
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.graphics.PixmapIO as __PixmapIO_PNG
__PNG = __PixmapIO_PNG.PNG
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PNG(pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.PixmapIO.PNG"""
 
    @staticmethod
    def __wrap(java_value: __PNG) -> 'PNG':
        return PNG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PNG):
        """
        Dynamic initializer for PNG.
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
    def setFlipY(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.setFlipY(boolean)"""
        super(__PNG, self).setFlipY(__boolean.valueOf(arg0))

    @overload
    def write(self, arg0: 'FileHandle', arg1: 'Pixmap'):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.write(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap) throws java.io.IOException"""
        super(__PNG, self).write(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.PixmapIO$PNG()"""
        val = __PNG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.PixmapIO$PNG(int)"""
        val = __PNG(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setCompression(self, arg0: int):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.setCompression(int)"""
        super(__PNG, self).setCompression(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.PixmapIO$PNG()"""
        val = __PNG()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def write(self, arg0: 'OutputStream', arg1: 'Pixmap'):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.write(java.io.OutputStream,com.badlogic.gdx.graphics.Pixmap) throws java.io.IOException"""
        super(__PNG, self).write(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.PixmapIO$PNG.dispose()"""
        super(PNG, self).dispose()

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.Color
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Color():
    """com.badlogic.gdx.graphics.Color"""
 
    @staticmethod
    def __wrap(java_value: __Color) -> 'Color':
        return Color(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Color):
        """
        Dynamic initializer for Color.
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
    def __init__(self, arg0: 'Color'):
        """public com.badlogic.gdx.graphics.Color(com.badlogic.gdx.graphics.Color)"""
        val = __Color(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def fromHsv(self, arg0: float, arg1: float, arg2: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.fromHsv(float,float,float)"""
        return 'Color'.__wrap(super(__Color, self).fromHsv(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def toFloatBits(self) -> float:
        """public float com.badlogic.gdx.graphics.Color.toFloatBits()"""
        return float.__wrap(super(Color, self).toFloatBits())

    @staticmethod
    @overload
    def abgr8888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.abgr8888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        __Color.abgr8888ToColor(arg0, __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.Color()"""
        val = __Color()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def rgb565(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb565(com.badlogic.gdx.graphics.Color)"""
        return int.__wrap(__Color.rgb565(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def argb8888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.argb8888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        __Color.argb8888ToColor(arg0, __int.valueOf(arg1))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.add(float,float,float,float)"""
        return 'Color'.__wrap(super(__Color, self).add(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def rgba8888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgba8888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        __Color.rgba8888ToColor(arg0, __int.valueOf(arg1))

    @overload
    def lerp(self, arg0: 'Color', arg1: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.lerp(com.badlogic.gdx.graphics.Color,float)"""
        return 'Color'.__wrap(super(__Color, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def set(self, arg0: int) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.set(int)"""
        return 'Color'.__wrap(super(__Color, self).set(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def rgb565(arg0: float, arg1: float, arg2: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb565(float,float,float)"""
        return int.__wrap(__Color.rgb565(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def rgba4444ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgba4444ToColor(com.badlogic.gdx.graphics.Color,int)"""
        __Color.rgba4444ToColor(arg0, __int.valueOf(arg1))

    @overload
    def mul(self, arg0: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.mul(float)"""
        return 'Color'.__wrap(super(__Color, self).mul(__float.valueOf(arg0)))

    @overload
    def fromHsv(self, arg0: 'float') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.fromHsv(float[])"""
        return 'Color'.__wrap(super(__Color, self).fromHsv(arg0))

    @overload
    def mul(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.mul(com.badlogic.gdx.graphics.Color)"""
        return 'Color'.__wrap(super(__Color, self).mul(arg0))

    @staticmethod
    @overload
    def rgba8888(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba8888(com.badlogic.gdx.graphics.Color)"""
        return int.__wrap(__Color.rgba8888(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.Color.equals(java.lang.Object)"""
        return bool.__wrap(super(__Color, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.Color(int)"""
        val = __Color(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def rgba4444(arg0: float, arg1: float, arg2: float, arg3: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba4444(float,float,float,float)"""
        return int.__wrap(__Color.rgba4444(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def argb8888(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.argb8888(com.badlogic.gdx.graphics.Color)"""
        return int.__wrap(__Color.argb8888(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.Color.toString()"""
        return str.__wrap(super(Color, self).toString())

    @staticmethod
    @overload
    def toFloatBits(arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public static float com.badlogic.gdx.graphics.Color.toFloatBits(float,float,float,float)"""
        return float.__wrap(__Color.toFloatBits(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def rgb888(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb888(com.badlogic.gdx.graphics.Color)"""
        return int.__wrap(__Color.rgb888(arg0))

    @overload
    def sub(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.sub(float,float,float,float)"""
        return 'Color'.__wrap(super(__Color, self).sub(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def rgb565ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgb565ToColor(com.badlogic.gdx.graphics.Color,int)"""
        __Color.rgb565ToColor(arg0, __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def toIntBits(self) -> int:
        """public int com.badlogic.gdx.graphics.Color.toIntBits()"""
        return int.__wrap(super(Color, self).toIntBits())

    @staticmethod
    @overload
    def toIntBits(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int com.badlogic.gdx.graphics.Color.toIntBits(int,int,int,int)"""
        return int.__wrap(__Color.toIntBits(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def mul(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.mul(float,float,float,float)"""
        return 'Color'.__wrap(super(__Color, self).mul(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def lerp(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.lerp(float,float,float,float,float)"""
        return 'Color'.__wrap(super(__Color, self).lerp(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @staticmethod
    @overload
    def rgba8888(arg0: float, arg1: float, arg2: float, arg3: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba8888(float,float,float,float)"""
        return int.__wrap(__Color.rgba8888(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def abgr8888ToColor(arg0: 'Color', arg1: float):
        """public static void com.badlogic.gdx.graphics.Color.abgr8888ToColor(com.badlogic.gdx.graphics.Color,float)"""
        __Color.abgr8888ToColor(arg0, __float.valueOf(arg1))

    @overload
    def premultiplyAlpha(self) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.premultiplyAlpha()"""
        return 'Color'.__wrap(super(Color, self).premultiplyAlpha())

    @overload
    def sub(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.sub(com.badlogic.gdx.graphics.Color)"""
        return 'Color'.__wrap(super(__Color, self).sub(arg0))

    @overload
    def cpy(self) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.cpy()"""
        return 'Color'.__wrap(super(Color, self).cpy())

    @staticmethod
    @overload
    def rgba4444(arg0: 'Color') -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgba4444(com.badlogic.gdx.graphics.Color)"""
        return int.__wrap(__Color.rgba4444(arg0))

    @overload
    def toHsv(self, arg0: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Color.toHsv(float[])"""
        return List[float].__wrap(super(__Color, self).toHsv(arg0))

    @staticmethod
    @overload
    def alpha(arg0: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.alpha(float)"""
        return int.__wrap(__Color.alpha(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def argb8888(arg0: float, arg1: float, arg2: float, arg3: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.argb8888(float,float,float,float)"""
        return int.__wrap(__Color.argb8888(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def luminanceAlpha(arg0: float, arg1: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.luminanceAlpha(float,float)"""
        return int.__wrap(__Color.luminanceAlpha(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.Color.hashCode()"""
        return int.__wrap(super(Color, self).hashCode())

    @overload
    def clamp(self) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.clamp()"""
        return 'Color'.__wrap(super(Color, self).clamp())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.valueOf(java.lang.String)"""
        return Color.__wrap(__Color.valueOf(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.set(float,float,float,float)"""
        return 'Color'.__wrap(super(__Color, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.graphics.Color(float,float,float,float)"""
        val = __Color(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.set(com.badlogic.gdx.graphics.Color)"""
        return 'Color'.__wrap(super(__Color, self).set(arg0))

    @staticmethod
    @overload
    def rgb888ToColor(arg0: 'Color', arg1: int):
        """public static void com.badlogic.gdx.graphics.Color.rgb888ToColor(com.badlogic.gdx.graphics.Color,int)"""
        __Color.rgb888ToColor(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def toFloatBits(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static float com.badlogic.gdx.graphics.Color.toFloatBits(int,int,int,int)"""
        return float.__wrap(__Color.toFloatBits(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.Color()"""
        val = __Color()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def rgb888(arg0: float, arg1: float, arg2: float) -> int:
        """public static int com.badlogic.gdx.graphics.Color.rgb888(float,float,float)"""
        return int.__wrap(__Color.rgb888(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def valueOf(arg0: str, arg1: 'Color') -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.valueOf(java.lang.String,com.badlogic.gdx.graphics.Color)"""
        return Color.__wrap(__Color.valueOf(arg0, arg1))

    @overload
    def add(self, arg0: 'Color') -> 'Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Color.add(com.badlogic.gdx.graphics.Color)"""
        return 'Color'.__wrap(super(__Color, self).add(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.Colors
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.ObjectMap as __ObjectMap
__ObjectMap = __ObjectMap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Colors as __Colors
__Colors = __Colors
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Colors():
    """com.badlogic.gdx.graphics.Colors"""
 
    @staticmethod
    def __wrap(java_value: __Colors) -> 'Colors':
        return Colors(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Colors):
        """
        Dynamic initializer for Colors.
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
        def reset():
            """public static void com.badlogic.gdx.graphics.Colors.reset()"""
            __Colors.reset()

    @staticmethod
    @overload
    def get(arg0: str) -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Colors.get(java.lang.String)"""
        return Color.__wrap(__Colors.get(arg0))

    @staticmethod
    @overload
    def getColors() -> 'utils.ObjectMap':
        """public static com.badlogic.gdx.utils.ObjectMap<java.lang.String, com.badlogic.gdx.graphics.Color> com.badlogic.gdx.graphics.Colors.getColors()"""
        return utils.ObjectMap.__wrap(__Colors.getColors())

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

    @staticmethod
    @overload
    def put(arg0: str, arg1: 'Color') -> 'Color':
        """public static com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.Colors.put(java.lang.String,com.badlogic.gdx.graphics.Color)"""
        return Color.__wrap(__Colors.put(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.Mesh$VertexDataType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import com.badlogic.gdx.graphics.Mesh as __Mesh_VertexDataType
__VertexDataType = __Mesh_VertexDataType.VertexDataType
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class VertexDataType(__Enum, Enum):
    """com.badlogic.gdx.graphics.Mesh.VertexDataType"""
 
    @staticmethod
    def __wrap(java_value: __VertexDataType) -> 'VertexDataType':
        return VertexDataType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexDataType):
        """
        Dynamic initializer for VertexDataType.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['VertexDataType']:
        """public static com.badlogic.gdx.graphics.Mesh$VertexDataType[] com.badlogic.gdx.graphics.Mesh$VertexDataType.values()"""
        return List[VertexDataType].__wrap(__VertexDataType.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'VertexDataType':
        """public static com.badlogic.gdx.graphics.Mesh$VertexDataType com.badlogic.gdx.graphics.Mesh$VertexDataType.valueOf(java.lang.String)"""
        return VertexDataType.__wrap(__VertexDataType.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.VertexAttribute
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.VertexAttribute as __VertexAttribute
__VertexAttribute = __VertexAttribute
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class VertexAttribute():
    """com.badlogic.gdx.graphics.VertexAttribute"""
 
    @staticmethod
    def __wrap(java_value: __VertexAttribute) -> 'VertexAttribute':
        return VertexAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexAttribute):
        """
        Dynamic initializer for VertexAttribute.
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
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: str, arg5: int):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,int,boolean,java.lang.String,int)"""
        val = __VertexAttribute(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), arg4, __int.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ColorUnpacked() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.ColorUnpacked()"""
        return VertexAttribute.__wrap(__VertexAttribute.ColorUnpacked())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,java.lang.String)"""
        val = __VertexAttribute(__int.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def BoneWeight(arg0: int) -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.BoneWeight(int)"""
        return VertexAttribute.__wrap(__VertexAttribute.BoneWeight(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def Normal() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Normal()"""
        return VertexAttribute.__wrap(__VertexAttribute.Normal())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.VertexAttribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__VertexAttribute, self).equals(arg0))

    @staticmethod
    @overload
    def ColorPacked() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.ColorPacked()"""
        return VertexAttribute.__wrap(__VertexAttribute.ColorPacked())

    @staticmethod
    @overload
    def Tangent() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Tangent()"""
        return VertexAttribute.__wrap(__VertexAttribute.Tangent())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getKey(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttribute.getKey()"""
        return int.__wrap(super(VertexAttribute, self).getKey())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: bool, arg4: str):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,int,boolean,java.lang.String)"""
        val = __VertexAttribute(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def copy(self) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.copy()"""
        return 'VertexAttribute'.__wrap(super(VertexAttribute, self).copy())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def Binormal() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Binormal()"""
        return VertexAttribute.__wrap(__VertexAttribute.Binormal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: int):
        """public com.badlogic.gdx.graphics.VertexAttribute(int,int,java.lang.String,int)"""
        val = __VertexAttribute(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttribute.hashCode()"""
        return int.__wrap(super(VertexAttribute, self).hashCode())

    @staticmethod
    @overload
    def Position() -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.Position()"""
        return VertexAttribute.__wrap(__VertexAttribute.Position())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSizeInBytes(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttribute.getSizeInBytes()"""
        return int.__wrap(super(VertexAttribute, self).getSizeInBytes())

    @overload
    def equals(self, arg0: 'VertexAttribute') -> bool:
        """public boolean com.badlogic.gdx.graphics.VertexAttribute.equals(com.badlogic.gdx.graphics.VertexAttribute)"""
        return bool.__wrap(super(__VertexAttribute, self).equals(arg0))

    @staticmethod
    @overload
    def TexCoords(arg0: int) -> 'VertexAttribute':
        """public static com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttribute.TexCoords(int)"""
        return VertexAttribute.__wrap(__VertexAttribute.TexCoords(__int.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.graphics.Cubemap
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.Texture as __Texture_TextureFilter
__TextureFilter = __Texture_TextureFilter.TextureFilter
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.Cubemap as __Cubemap
__Cubemap = __Cubemap
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.CubemapData as __CubemapData
__CubemapData = __CubemapData
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture_TextureWrap
__TextureWrap = __Texture_TextureWrap.TextureWrap
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class Cubemap(__GLTexture, GLTexture):
    """com.badlogic.gdx.graphics.Cubemap"""
 
    @staticmethod
    def __wrap(java_value: __Cubemap) -> 'Cubemap':
        return Cubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cubemap):
        """
        Dynamic initializer for Cubemap.
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
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap.getHeight()"""
        return int.__wrap(super(Cubemap, self).getHeight())

    @override
    @overload
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getVWrap())

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1, __boolean.valueOf(arg2))

    @staticmethod
    @overload
    def invalidateAllCubemaps(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Cubemap.invalidateAllCubemaps(com.badlogic.gdx.Application)"""
        __Cubemap.invalidateAllCubemaps(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Cubemap.isManaged()"""
        return bool.__wrap(super(Cubemap, self).isManaged())

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1)

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(__GLTexture, self).bind(__int.valueOf(arg0))

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).setAnisotropicFilter(__float.valueOf(arg0)))

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMagFilter())

    @overload
    def getCubemapData(self) -> 'CubemapData':
        """public com.badlogic.gdx.graphics.CubemapData com.badlogic.gdx.graphics.Cubemap.getCubemapData()"""
        return 'CubemapData'.__wrap(super(Cubemap, self).getCubemapData())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap.getDepth()"""
        return int.__wrap(super(Cubemap, self).getDepth())

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap.getWidth()"""
        return int.__wrap(super(Cubemap, self).getWidth())

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap)"""
        val = __Cubemap(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self, arg0: 'CubemapData'):
        """public void com.badlogic.gdx.graphics.Cubemap.load(com.badlogic.gdx.graphics.CubemapData)"""
        super(__Cubemap, self).load(arg0)

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def setAssetManager(arg0: 'AssetManager'):
        """public static void com.badlogic.gdx.graphics.Cubemap.setAssetManager(com.badlogic.gdx.assets.AssetManager)"""
        __Cubemap.setAssetManager(arg0)

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle', arg6: bool):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __Cubemap(arg0, arg1, arg2, arg3, arg4, arg5, __boolean.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: 'Format'):
        """public com.badlogic.gdx.graphics.Cubemap(int,int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = __Cubemap(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).setFilter(arg0, arg1)

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float.__wrap(__GLTexture.getMaxAnisotropicFilterLevel())

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).setWrap(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Cubemap.dispose()"""
        super(Cubemap, self).dispose()

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        __GLTexture.uploadImageData(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getUWrap())

    @overload
    def __init__(self, arg0: 'CubemapData'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.CubemapData)"""
        val = __Cubemap(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMinFilter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float.__wrap(super(GLTexture, self).getAnisotropicFilter())

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Pixmap', arg2: 'Pixmap', arg3: 'Pixmap', arg4: 'Pixmap', arg5: 'Pixmap', arg6: bool):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap,boolean)"""
        val = __Cubemap(arg0, arg1, arg2, arg3, arg4, arg5, __boolean.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getNumManagedCubemaps() -> int:
        """public static int com.badlogic.gdx.graphics.Cubemap.getNumManagedCubemaps()"""
        return int.__wrap(__Cubemap.getNumManagedCubemaps())

    @overload
    def __init__(self, arg0: 'TextureData', arg1: 'TextureData', arg2: 'TextureData', arg3: 'TextureData', arg4: 'TextureData', arg5: 'TextureData'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData,com.badlogic.gdx.graphics.TextureData)"""
        val = __Cubemap(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Cubemap.getManagedStatus()"""
        return str.__wrap(__Cubemap.getManagedStatus())

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: 'FileHandle', arg3: 'FileHandle', arg4: 'FileHandle', arg5: 'FileHandle'):
        """public com.badlogic.gdx.graphics.Cubemap(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __Cubemap(arg0, arg1, arg2, arg3, arg4, arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def clearAllCubemaps(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Cubemap.clearAllCubemaps(com.badlogic.gdx.Application)"""
        __Cubemap.clearAllCubemaps(arg0)

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int.__wrap(super(GLTexture, self).getTextureObjectHandle()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Cursor
import com.badlogic.gdx.graphics.Cursor as __Cursor
__Cursor = __Cursor
from abc import abstractmethod, ABC
import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class Cursor(ABC, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.Cursor"""
 
    @staticmethod
    def __wrap(java_value: __Cursor) -> 'Cursor':
        return Cursor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Cursor):
        """
        Dynamic initializer for Cursor.
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
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.FPSLogger
import com.badlogic.gdx.graphics.FPSLogger as __FPSLogger
__FPSLogger = __FPSLogger
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FPSLogger():
    """com.badlogic.gdx.graphics.FPSLogger"""
 
    @staticmethod
    def __wrap(java_value: __FPSLogger) -> 'FPSLogger':
        return FPSLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FPSLogger):
        """
        Dynamic initializer for FPSLogger.
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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.FPSLogger(int)"""
        val = __FPSLogger(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def log(self):
        """public void com.badlogic.gdx.graphics.FPSLogger.log()"""
        super(FPSLogger, self).log()

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.FPSLogger()"""
        val = __FPSLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.FPSLogger()"""
        val = __FPSLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureData$Factory
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.TextureData as __TextureData_Factory
__Factory = __TextureData_Factory.Factory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.TextureData as __TextureData
__TextureData = __TextureData
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Factory():
    """com.badlogic.gdx.graphics.TextureData.Factory"""
 
    @staticmethod
    def __wrap(java_value: __Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Factory):
        """
        Dynamic initializer for Factory.
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
    def loadFromFile(arg0: 'FileHandle', arg1: bool) -> 'TextureData':
        """public static com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.TextureData$Factory.loadFromFile(com.badlogic.gdx.files.FileHandle,boolean)"""
        return TextureData.__wrap(__Factory.loadFromFile(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.TextureData$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def loadFromFile(arg0: 'FileHandle', arg1: 'Format', arg2: bool) -> 'TextureData':
        """public static com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.TextureData$Factory.loadFromFile(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        return TextureData.__wrap(__Factory.loadFromFile(arg0, arg1, __boolean.valueOf(arg2)))

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.TextureData$Factory()"""
        val = __Factory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.GLTexture
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.Texture as __Texture_TextureFilter
__TextureFilter = __Texture_TextureFilter.TextureFilter
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture_TextureWrap
__TextureWrap = __Texture_TextureWrap.TextureWrap
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLTexture(ABC, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.GLTexture"""
 
    @staticmethod
    def __wrap(java_value: __GLTexture) -> 'GLTexture':
        return GLTexture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLTexture):
        """
        Dynamic initializer for GLTexture.
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
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getVWrap())

    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.GLTexture(int,int)"""
        val = __GLTexture(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMagFilter())

    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMinFilter())

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).setAnisotropicFilter(__float.valueOf(arg0)))

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

    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.GLTexture.dispose()"""
        super(GLTexture, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1)

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float.__wrap(__GLTexture.getMaxAnisotropicFilterLevel())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.GLTexture(int)"""
        val = __GLTexture(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1, __boolean.valueOf(arg2))

    @abstractmethod
    def getDepth(self, ):
        """public abstract int com.badlogic.gdx.graphics.GLTexture.getDepth()"""
        pass

    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int.__wrap(super(GLTexture, self).getTextureObjectHandle())

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        __GLTexture.uploadImageData(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float.__wrap(super(GLTexture, self).getAnisotropicFilter())

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.GLTexture.getWidth()"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).setFilter(arg0, arg1)

    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1)

    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).setWrap(arg0, arg1)

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0), __boolean.valueOf(arg1)))

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.GLTexture.isManaged()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(__GLTexture, self).bind(__int.valueOf(arg0))

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.GLTexture.getHeight()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureData$TextureDataType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.graphics.TextureData as __TextureData_TextureDataType
__TextureDataType = __TextureData_TextureDataType.TextureDataType
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class TextureDataType(__Enum, Enum):
    """com.badlogic.gdx.graphics.TextureData.TextureDataType"""
 
    @staticmethod
    def __wrap(java_value: __TextureDataType) -> 'TextureDataType':
        return TextureDataType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureDataType):
        """
        Dynamic initializer for TextureDataType.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextureDataType':
        """public static com.badlogic.gdx.graphics.TextureData$TextureDataType com.badlogic.gdx.graphics.TextureData$TextureDataType.valueOf(java.lang.String)"""
        return TextureDataType.__wrap(__TextureDataType.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['TextureDataType']:
        """public static com.badlogic.gdx.graphics.TextureData$TextureDataType[] com.badlogic.gdx.graphics.TextureData$TextureDataType.values()"""
        return List[TextureDataType].__wrap(__TextureDataType.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$Filter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Filter
__Filter = __Pixmap_Filter.Filter
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Filter(__Enum, Enum):
    """com.badlogic.gdx.graphics.Pixmap.Filter"""
 
    @staticmethod
    def __wrap(java_value: __Filter) -> 'Filter':
        return Filter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Filter):
        """
        Dynamic initializer for Filter.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Filter':
        """public static com.badlogic.gdx.graphics.Pixmap$Filter com.badlogic.gdx.graphics.Pixmap$Filter.valueOf(java.lang.String)"""
        return Filter.__wrap(__Filter.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['Filter']:
        """public static com.badlogic.gdx.graphics.Pixmap$Filter[] com.badlogic.gdx.graphics.Pixmap$Filter.values()"""
        return List[Filter].__wrap(__Filter.values())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Pixmap$Blending
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Blending
__Blending = __Pixmap_Blending.Blending
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Blending(__Enum, Enum):
    """com.badlogic.gdx.graphics.Pixmap.Blending"""
 
    @staticmethod
    def __wrap(java_value: __Blending) -> 'Blending':
        return Blending(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Blending):
        """
        Dynamic initializer for Blending.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def values() -> List['Blending']:
        """public static com.badlogic.gdx.graphics.Pixmap$Blending[] com.badlogic.gdx.graphics.Pixmap$Blending.values()"""
        return List[Blending].__wrap(__Blending.values())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Blending':
        """public static com.badlogic.gdx.graphics.Pixmap$Blending com.badlogic.gdx.graphics.Pixmap$Blending.valueOf(java.lang.String)"""
        return Blending.__wrap(__Blending.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Texture
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.Texture as __Texture_TextureFilter
__TextureFilter = __Texture_TextureFilter.TextureFilter
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.TextureData as __TextureData
__TextureData = __TextureData
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import com.badlogic.gdx.graphics.Texture as __Texture_TextureWrap
__TextureWrap = __Texture_TextureWrap.TextureWrap
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class Texture(__GLTexture, GLTexture):
    """com.badlogic.gdx.graphics.Texture"""
 
    @staticmethod
    def __wrap(java_value: __Texture) -> 'Texture':
        return Texture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Texture):
        """
        Dynamic initializer for Texture.
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
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def setAssetManager(arg0: 'AssetManager'):
        """public static void com.badlogic.gdx.graphics.Texture.setAssetManager(com.badlogic.gdx.assets.AssetManager)"""
        __Texture.setAssetManager(arg0)

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(__GLTexture, self).bind(__int.valueOf(arg0))

    @overload
    def getTextureData(self) -> 'TextureData':
        """public com.badlogic.gdx.graphics.TextureData com.badlogic.gdx.graphics.Texture.getTextureData()"""
        return 'TextureData'.__wrap(super(Texture, self).getTextureData())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Texture.isManaged()"""
        return bool.__wrap(super(Texture, self).isManaged())

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).setAnisotropicFilter(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.Texture(java.lang.String)"""
        val = __Texture(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Texture.dispose()"""
        super(Texture, self).dispose()

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).setFilter(arg0, arg1)

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMinFilter())

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.Pixmap,boolean)"""
        val = __Texture(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __Texture(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def clearAllTextures(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture.clearAllTextures(com.badlogic.gdx.Application)"""
        __Texture.clearAllTextures(arg0)

    @overload
    def __init__(self, arg0: 'TextureData'):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.TextureData)"""
        val = __Texture(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int.__wrap(super(GLTexture, self).getTextureObjectHandle())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture.getWidth()"""
        return int.__wrap(super(Texture, self).getWidth())

    @overload
    def draw(self, arg0: 'Pixmap', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Texture.draw(com.badlogic.gdx.graphics.Pixmap,int,int)"""
        super(__Texture, self).draw(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getVWrap())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'Format', arg2: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        val = __Texture(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1)

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMagFilter())

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1, __boolean.valueOf(arg2))

    @staticmethod
    @overload
    def getNumManagedTextures() -> int:
        """public static int com.badlogic.gdx.graphics.Texture.getNumManagedTextures()"""
        return int.__wrap(__Texture.getNumManagedTextures())

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.files.FileHandle)"""
        val = __Texture(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format'):
        """public com.badlogic.gdx.graphics.Texture(int,int,com.badlogic.gdx.graphics.Pixmap$Format)"""
        val = __Texture(__int.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Texture.getManagedStatus()"""
        return str.__wrap(__Texture.getManagedStatus())

    @staticmethod
    @overload
    def invalidateAllTextures(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Texture.invalidateAllTextures(com.badlogic.gdx.Application)"""
        __Texture.invalidateAllTextures(arg0)

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float.__wrap(__GLTexture.getMaxAnisotropicFilterLevel())

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture.getDepth()"""
        return int.__wrap(super(Texture, self).getDepth())

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).setWrap(arg0, arg1)

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.Texture.getHeight()"""
        return int.__wrap(super(Texture, self).getHeight())

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        __GLTexture.uploadImageData(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.Texture.toString()"""
        return str.__wrap(super(Texture, self).toString())

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float.__wrap(super(GLTexture, self).getAnisotropicFilter())

    @overload
    def __init__(self, arg0: 'Pixmap', arg1: 'Format', arg2: bool):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.Pixmap,com.badlogic.gdx.graphics.Pixmap$Format,boolean)"""
        val = __Texture(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self, arg0: 'TextureData'):
        """public void com.badlogic.gdx.graphics.Texture.load(com.badlogic.gdx.graphics.TextureData)"""
        super(__Texture, self).load(arg0)

    @overload
    def __init__(self, arg0: 'Pixmap'):
        """public com.badlogic.gdx.graphics.Texture(com.badlogic.gdx.graphics.Pixmap)"""
        val = __Texture(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.Cubemap$CubemapSide
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
import com.badlogic.gdx.graphics.Cubemap as __Cubemap_CubemapSide
__CubemapSide = __Cubemap_CubemapSide.CubemapSide
from builtins import int
 
class CubemapSide(__Enum, Enum):
    """com.badlogic.gdx.graphics.Cubemap.CubemapSide"""
 
    @staticmethod
    def __wrap(java_value: __CubemapSide) -> 'CubemapSide':
        return CubemapSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CubemapSide):
        """
        Dynamic initializer for CubemapSide.
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
    def values() -> List['CubemapSide']:
        """public static com.badlogic.gdx.graphics.Cubemap$CubemapSide[] com.badlogic.gdx.graphics.Cubemap$CubemapSide.values()"""
        return List[CubemapSide].__wrap(__CubemapSide.values())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CubemapSide':
        """public static com.badlogic.gdx.graphics.Cubemap$CubemapSide com.badlogic.gdx.graphics.Cubemap$CubemapSide.valueOf(java.lang.String)"""
        return CubemapSide.__wrap(__CubemapSide.valueOf(arg0))

    @overload
    def getUp(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Cubemap$CubemapSide.getUp(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__CubemapSide, self).getUp(arg0))

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getDirection(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.Cubemap$CubemapSide.getDirection(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__CubemapSide, self).getDirection(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @overload
    def getGLEnum(self) -> int:
        """public int com.badlogic.gdx.graphics.Cubemap$CubemapSide.getGLEnum()"""
        return int.__wrap(super(CubemapSide, self).getGLEnum()) 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureArray
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.Texture as __Texture_TextureFilter
__TextureFilter = __Texture_TextureFilter.TextureFilter
import com.badlogic.gdx.graphics.GLTexture as __GLTexture
__GLTexture = __GLTexture
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture_TextureWrap
__TextureWrap = __Texture_TextureWrap.TextureWrap
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
import com.badlogic.gdx.graphics.TextureArray as __TextureArray
__TextureArray = __TextureArray
from builtins import int
 
class TextureArray(__GLTexture, GLTexture):
    """com.badlogic.gdx.graphics.TextureArray"""
 
    @staticmethod
    def __wrap(java_value: __TextureArray) -> 'TextureArray':
        return TextureArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureArray):
        """
        Dynamic initializer for TextureArray.
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
    def getVWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getVWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getVWrap())

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap,boolean)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1)

    @override
    @overload
    def getDepth(self) -> int:
        """public int com.badlogic.gdx.graphics.TextureArray.getDepth()"""
        return int.__wrap(super(TextureArray, self).getDepth())

    @override
    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.TextureArray.getHeight()"""
        return int.__wrap(super(TextureArray, self).getHeight())

    @overload
    def __init__(self, arg0: 'TextureArrayData'):
        """public com.badlogic.gdx.graphics.TextureArray(com.badlogic.gdx.graphics.TextureArrayData)"""
        val = __TextureArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def bind(self, arg0: int):
        """public void com.badlogic.gdx.graphics.GLTexture.bind(int)"""
        super(__GLTexture, self).bind(__int.valueOf(arg0))

    @override
    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.TextureArray.getWidth()"""
        return int.__wrap(super(TextureArray, self).getWidth())

    @overload
    def setAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.setAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).setAnisotropicFilter(__float.valueOf(arg0)))

    @override
    @overload
    def getMagFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMagFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMagFilter())

    @staticmethod
    @overload
    def getNumManagedTextureArrays() -> int:
        """public static int com.badlogic.gdx.graphics.TextureArray.getNumManagedTextureArrays()"""
        return int.__wrap(__TextureArray.getNumManagedTextureArrays())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def unsafeSetFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__GLTexture, self).unsafeSetFilter(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def unsafeSetWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.unsafeSetWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).unsafeSetWrap(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, *arg0: str):
        """public com.badlogic.gdx.graphics.TextureArray(java.lang.String...)"""
        val = __TextureArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.GLTexture.dispose()"""
        super(GLTexture, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setFilter(self, arg0: 'TextureFilter', arg1: 'TextureFilter'):
        """public void com.badlogic.gdx.graphics.GLTexture.setFilter(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter)"""
        super(__GLTexture, self).setFilter(arg0, arg1)

    @staticmethod
    @overload
    def getMaxAnisotropicFilterLevel() -> float:
        """public static float com.badlogic.gdx.graphics.GLTexture.getMaxAnisotropicFilterLevel()"""
        return float.__wrap(__GLTexture.getMaxAnisotropicFilterLevel())

    @override
    @overload
    def isManaged(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.TextureArray.isManaged()"""
        return bool.__wrap(super(TextureArray, self).isManaged())

    @override
    @overload
    def setWrap(self, arg0: 'TextureWrap', arg1: 'TextureWrap'):
        """public void com.badlogic.gdx.graphics.GLTexture.setWrap(com.badlogic.gdx.graphics.Texture$TextureWrap,com.badlogic.gdx.graphics.Texture$TextureWrap)"""
        super(__GLTexture, self).setWrap(arg0, arg1)

    @overload
    def __init__(self, *arg0: 'files.FileHandle'):
        """public com.badlogic.gdx.graphics.TextureArray(com.badlogic.gdx.files.FileHandle...)"""
        val = __TextureArray(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool, arg1: 'Format', *arg2: 'files.FileHandle'):
        """public com.badlogic.gdx.graphics.TextureArray(boolean,com.badlogic.gdx.graphics.Pixmap$Format,com.badlogic.gdx.files.FileHandle...)"""
        val = __TextureArray(__boolean.valueOf(arg0), arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def uploadImageData(arg0: int, arg1: 'TextureData', arg2: int):
        """public static void com.badlogic.gdx.graphics.GLTexture.uploadImageData(int,com.badlogic.gdx.graphics.TextureData,int)"""
        __GLTexture.uploadImageData(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getUWrap(self) -> 'TextureWrap':
        """public com.badlogic.gdx.graphics.Texture$TextureWrap com.badlogic.gdx.graphics.GLTexture.getUWrap()"""
        return 'TextureWrap'.__wrap(super(GLTexture, self).getUWrap())

    @override
    @overload
    def bind(self):
        """public void com.badlogic.gdx.graphics.GLTexture.bind()"""
        super(GLTexture, self).bind()

    @override
    @overload
    def getMinFilter(self) -> 'TextureFilter':
        """public com.badlogic.gdx.graphics.Texture$TextureFilter com.badlogic.gdx.graphics.GLTexture.getMinFilter()"""
        return 'TextureFilter'.__wrap(super(GLTexture, self).getMinFilter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getAnisotropicFilter(self) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.getAnisotropicFilter()"""
        return float.__wrap(super(GLTexture, self).getAnisotropicFilter())

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.TextureArray.getManagedStatus()"""
        return str.__wrap(__TextureArray.getManagedStatus())

    @staticmethod
    @overload
    def clearAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.TextureArray.clearAllTextureArrays(com.badlogic.gdx.Application)"""
        __TextureArray.clearAllTextureArrays(arg0)

    @overload
    def __init__(self, arg0: bool, *arg1: 'files.FileHandle'):
        """public com.badlogic.gdx.graphics.TextureArray(boolean,com.badlogic.gdx.files.FileHandle...)"""
        val = __TextureArray(__boolean.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def unsafeSetAnisotropicFilter(self, arg0: float, arg1: bool) -> float:
        """public float com.badlogic.gdx.graphics.GLTexture.unsafeSetAnisotropicFilter(float,boolean)"""
        return float.__wrap(super(__GLTexture, self).unsafeSetAnisotropicFilter(__float.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def invalidateAllTextureArrays(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.TextureArray.invalidateAllTextureArrays(com.badlogic.gdx.Application)"""
        __TextureArray.invalidateAllTextureArrays(arg0)

    @override
    @overload
    def getTextureObjectHandle(self) -> int:
        """public int com.badlogic.gdx.graphics.GLTexture.getTextureObjectHandle()"""
        return int.__wrap(super(GLTexture, self).getTextureObjectHandle()) 
 
 
# CLASS: com.badlogic.gdx.graphics.TextureArrayData
import com.badlogic.gdx.graphics.TextureArrayData as __TextureArrayData
__TextureArrayData = __TextureArrayData
from abc import abstractmethod, ABC
 
class TextureArrayData(ABC):
    """com.badlogic.gdx.graphics.TextureArrayData"""
 
    @staticmethod
    def __wrap(java_value: __TextureArrayData) -> 'TextureArrayData':
        return TextureArrayData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureArrayData):
        """
        Dynamic initializer for TextureArrayData.
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
    def prepare(self, ):
        """public abstract void com.badlogic.gdx.graphics.TextureArrayData.prepare()"""
        pass

    @abstractmethod
    def isPrepared(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureArrayData.isPrepared()"""
        pass

    @abstractmethod
    def getInternalFormat(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getInternalFormat()"""
        pass

    @abstractmethod
    def getWidth(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getWidth()"""
        pass

    @abstractmethod
    def consumeTextureArrayData(self, ):
        """public abstract void com.badlogic.gdx.graphics.TextureArrayData.consumeTextureArrayData()"""
        pass

    @abstractmethod
    def getHeight(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getHeight()"""
        pass

    @abstractmethod
    def isManaged(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.TextureArrayData.isManaged()"""
        pass

    @abstractmethod
    def getGLType(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getGLType()"""
        pass

    @abstractmethod
    def getDepth(self, ):
        """public abstract int com.badlogic.gdx.graphics.TextureArrayData.getDepth()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.VertexAttributes
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.VertexAttribute as __VertexAttribute
__VertexAttribute = __VertexAttribute
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class VertexAttributes(__Iterable, Iterable, __Comparable, Comparable):
    """com.badlogic.gdx.graphics.VertexAttributes"""
 
    @staticmethod
    def __wrap(java_value: __VertexAttributes) -> 'VertexAttributes':
        return VertexAttributes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __VertexAttributes):
        """
        Dynamic initializer for VertexAttributes.
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
    def get(self, arg0: int) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttributes.get(int)"""
        return 'VertexAttribute'.__wrap(super(__VertexAttributes, self).get(__int.valueOf(arg0)))

    @overload
    def getOffset(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getOffset(int)"""
        return int.__wrap(super(__VertexAttributes, self).getOffset(__int.valueOf(arg0)))

    @overload
    def findByUsage(self, arg0: int) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.VertexAttributes.findByUsage(int)"""
        return 'VertexAttribute'.__wrap(super(__VertexAttributes, self).findByUsage(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compareTo(self, arg0: 'VertexAttributes') -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.compareTo(com.badlogic.gdx.graphics.VertexAttributes)"""
        return int.__wrap(super(__VertexAttributes, self).compareTo(arg0))

    @overload
    def __init__(self, *arg0: 'VertexAttribute'):
        """public com.badlogic.gdx.graphics.VertexAttributes(com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __VertexAttributes(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getOffset(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getOffset(int,int)"""
        return int.__wrap(super(__VertexAttributes, self).getOffset(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getMaskWithSizePacked(self) -> int:
        """public long com.badlogic.gdx.graphics.VertexAttributes.getMaskWithSizePacked()"""
        return int.__wrap(super(VertexAttributes, self).getMaskWithSizePacked())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.VertexAttributes.equals(java.lang.Object)"""
        return bool.__wrap(super(__VertexAttributes, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<com.badlogic.gdx.graphics.VertexAttribute> com.badlogic.gdx.graphics.VertexAttributes.iterator()"""
        return 'Iterator'.__wrap(super(VertexAttributes, self).iterator())

    @overload
    def size(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.size()"""
        return int.__wrap(super(VertexAttributes, self).size())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.hashCode()"""
        return int.__wrap(super(VertexAttributes, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getBoneWeights(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getBoneWeights()"""
        return int.__wrap(super(VertexAttributes, self).getBoneWeights())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.VertexAttributes.toString()"""
        return str.__wrap(super(VertexAttributes, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def getMask(self) -> int:
        """public long com.badlogic.gdx.graphics.VertexAttributes.getMask()"""
        return int.__wrap(super(VertexAttributes, self).getMask())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def getTextureCoordinates(self) -> int:
        """public int com.badlogic.gdx.graphics.VertexAttributes.getTextureCoordinates()"""
        return int.__wrap(super(VertexAttributes, self).getTextureCoordinates()) 
 
 
# CLASS: com.badlogic.gdx.graphics.Mesh
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.VertexAttributes as __VertexAttributes
__VertexAttributes = __VertexAttributes
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.Mesh as __Mesh
__Mesh = __Mesh
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
from builtins import float
from typing import List
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.VertexAttribute as __VertexAttribute
__VertexAttribute = __VertexAttribute
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.lang.Integer as __int
from builtins import int
 
class Mesh(pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.Mesh"""
 
    @staticmethod
    def __wrap(java_value: __Mesh) -> 'Mesh':
        return Mesh(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Mesh):
        """
        Dynamic initializer for Mesh.
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
    def setVertices(self, arg0: 'float', arg1: int, arg2: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setVertices(float[],int,int)"""
        return 'Mesh'.__wrap(super(__Mesh, self).setVertices(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def updateVertices(self, arg0: int, arg1: 'float', arg2: int, arg3: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateVertices(int,float[],int,int)"""
        return 'Mesh'.__wrap(super(__Mesh, self).updateVertices(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def transform(self, arg0: 'Matrix4', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.Mesh.transform(com.badlogic.gdx.math.Matrix4,int,int)"""
        super(__Mesh, self).transform(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def copy(self, arg0: bool, arg1: bool, arg2: 'int') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.copy(boolean,boolean,int[])"""
        return 'Mesh'.__wrap(super(__Mesh, self).copy(__boolean.valueOf(arg0), __boolean.valueOf(arg1), arg2))

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int)"""
        return 'collision.BoundingBox'.__wrap(super(__Mesh, self).extendBoundingBox(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setInstanceData(self, arg0: 'FloatBuffer') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(java.nio.FloatBuffer)"""
        return 'Mesh'.__wrap(super(__Mesh, self).setInstanceData(arg0))

    @overload
    def getVertexAttribute(self, arg0: int) -> 'VertexAttribute':
        """public com.badlogic.gdx.graphics.VertexAttribute com.badlogic.gdx.graphics.Mesh.getVertexAttribute(int)"""
        return 'VertexAttribute'.__wrap(super(__Mesh, self).getVertexAttribute(__int.valueOf(arg0)))

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: int, arg2: int, arg3: int, arg4: bool):
        """public void com.badlogic.gdx.graphics.Mesh.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,int,int,int,boolean)"""
        super(__Mesh, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4))

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: int, arg3: int, arg4: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.Mesh(boolean,boolean,int,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __Mesh(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def unbind(self, arg0: 'ShaderProgram', arg1: 'int', arg2: 'int'):
        """public void com.badlogic.gdx.graphics.Mesh.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[],int[])"""
        super(__Mesh, self).unbind(arg0, arg1, arg2)

    @overload
    def getIndices(self, arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(int,int,short[],int)"""
        super(__Mesh, self).getIndices(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int)"""
        return 'collision.BoundingBox'.__wrap(super(__Mesh, self).calculateBoundingBox(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def transformUV(arg0: 'Matrix3', arg1: 'float', arg2: int, arg3: int, arg4: int, arg5: int):
        """public static void com.badlogic.gdx.graphics.Mesh.transformUV(com.badlogic.gdx.math.Matrix3,float[],int,int,int,int)"""
        __Mesh.transformUV(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def setIndices(self, arg0: 'short', arg1: int, arg2: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setIndices(short[],int,int)"""
        return 'Mesh'.__wrap(super(__Mesh, self).setIndices(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getNumVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getNumVertices()"""
        return int.__wrap(super(Mesh, self).getNumVertices())

    @overload
    def copy(self, arg0: bool) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.copy(boolean)"""
        return 'Mesh'.__wrap(super(__Mesh, self).copy(__boolean.valueOf(arg0)))

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: int):
        """public void com.badlogic.gdx.graphics.Mesh.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,int)"""
        super(__Mesh, self).render(arg0, __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def calculateRadiusSquared(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Matrix4') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadiusSquared(float,float,float,int,int,com.badlogic.gdx.math.Matrix4)"""
        return float.__wrap(super(__Mesh, self).calculateRadiusSquared(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @overload
    def calculateRadius(self, arg0: 'Vector3', arg1: int, arg2: int, arg3: 'Matrix4') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(com.badlogic.gdx.math.Vector3,int,int,com.badlogic.gdx.math.Matrix4)"""
        return float.__wrap(super(__Mesh, self).calculateRadius(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def isInstanced(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.Mesh.isInstanced()"""
        return bool.__wrap(super(Mesh, self).isInstanced())

    @overload
    def getIndices(self, arg0: int, arg1: 'short', arg2: int):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(int,short[],int)"""
        super(__Mesh, self).getIndices(__int.valueOf(arg0), arg1, __int.valueOf(arg2))

    @overload
    def calculateRadius(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'Matrix4') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(float,float,float,int,int,com.badlogic.gdx.math.Matrix4)"""
        return float.__wrap(super(__Mesh, self).calculateRadius(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @overload
    def __init__(self, arg0: 'VertexDataType', arg1: bool, arg2: int, arg3: int, *arg4: 'VertexAttribute'):
        """public com.badlogic.gdx.graphics.Mesh(com.badlogic.gdx.graphics.Mesh$VertexDataType,boolean,int,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __Mesh(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setVertices(self, arg0: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setVertices(float[])"""
        return 'Mesh'.__wrap(super(__Mesh, self).setVertices(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.Mesh.dispose()"""
        super(Mesh, self).dispose()

    @overload
    def render(self, arg0: 'ShaderProgram', arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.Mesh.render(com.badlogic.gdx.graphics.glutils.ShaderProgram,int,int,int)"""
        super(__Mesh, self).render(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def calculateRadius(self, arg0: float, arg1: float, arg2: float) -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(float,float,float)"""
        return float.__wrap(super(__Mesh, self).calculateRadius(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox'):
        """public void com.badlogic.gdx.graphics.Mesh.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        super(__Mesh, self).calculateBoundingBox(arg0)

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: int, *arg3: 'VertexAttribute'):
        """public com.badlogic.gdx.graphics.Mesh(boolean,int,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        val = __Mesh(__boolean.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def bind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.Mesh.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__Mesh, self).bind(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def enableInstancedRendering(self, arg0: bool, arg1: int, *arg2: 'VertexAttribute') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.enableInstancedRendering(boolean,int,com.badlogic.gdx.graphics.VertexAttribute...)"""
        return 'Mesh'.__wrap(super(__Mesh, self).enableInstancedRendering(__boolean.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,java.nio.FloatBuffer)"""
        return 'Mesh'.__wrap(super(__Mesh, self).updateInstanceData(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getVertices(self, arg0: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(float[])"""
        return List[float].__wrap(super(__Mesh, self).getVertices(arg0))

    @overload
    def getVertexSize(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getVertexSize()"""
        return int.__wrap(super(Mesh, self).getVertexSize())

    @overload
    def getIndicesBuffer(self, arg0: bool) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.Mesh.getIndicesBuffer(boolean)"""
        return 'ShortBuffer'.__wrap(super(__Mesh, self).getIndicesBuffer(__boolean.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'VertexDataType', arg1: bool, arg2: int, arg3: int, arg4: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.Mesh(com.badlogic.gdx.graphics.Mesh$VertexDataType,boolean,int,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __Mesh(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setInstanceData(self, arg0: 'float', arg1: int, arg2: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(float[],int,int)"""
        return 'Mesh'.__wrap(super(__Mesh, self).setInstanceData(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getMaxIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getMaxIndices()"""
        return int.__wrap(super(Mesh, self).getMaxIndices())

    @overload
    def getVertices(self, arg0: int, arg1: int, arg2: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(int,int,float[])"""
        return List[float].__wrap(super(__Mesh, self).getVertices(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @overload
    def getIndices(self, arg0: 'short'):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(short[])"""
        super(__Mesh, self).getIndices(arg0)

    @overload
    def getNumIndices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getNumIndices()"""
        return int.__wrap(super(Mesh, self).getNumIndices())

    @overload
    def bind(self, arg0: 'ShaderProgram', arg1: 'int', arg2: 'int'):
        """public void com.badlogic.gdx.graphics.Mesh.bind(com.badlogic.gdx.graphics.glutils.ShaderProgram,int[],int[])"""
        super(__Mesh, self).bind(arg0, arg1, arg2)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def transform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.Mesh.transform(com.badlogic.gdx.math.Matrix4)"""
        super(__Mesh, self).transform(arg0)

    @overload
    def getIndicesBuffer(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer com.badlogic.gdx.graphics.Mesh.getIndicesBuffer()"""
        return 'ShortBuffer'.__wrap(super(Mesh, self).getIndicesBuffer())

    @overload
    def calculateRadius(self, arg0: float, arg1: float, arg2: float, arg3: int, arg4: int) -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(float,float,float,int,int)"""
        return float.__wrap(super(__Mesh, self).calculateRadius(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @overload
    def getVertices(self, arg0: int, arg1: 'float') -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(int,float[])"""
        return List[float].__wrap(super(__Mesh, self).getVertices(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getManagedStatus() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.Mesh.getManagedStatus()"""
        return str.__wrap(__Mesh.getManagedStatus())

    @overload
    def getVertices(self, arg0: int, arg1: int, arg2: 'float', arg3: int) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.Mesh.getVertices(int,int,float[],int)"""
        return List[float].__wrap(super(__Mesh, self).getVertices(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def invalidateAllMeshes(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Mesh.invalidateAllMeshes(com.badlogic.gdx.Application)"""
        __Mesh.invalidateAllMeshes(arg0)

    @overload
    def calculateBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.calculateBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(Mesh, self).calculateBoundingBox())

    @overload
    def getMaxVertices(self) -> int:
        """public int com.badlogic.gdx.graphics.Mesh.getMaxVertices()"""
        return int.__wrap(super(Mesh, self).getMaxVertices())

    @overload
    def setInstanceData(self, arg0: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(float[])"""
        return 'Mesh'.__wrap(super(__Mesh, self).setInstanceData(arg0))

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.Mesh.scale(float,float,float)"""
        super(__Mesh, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def calculateRadius(self, arg0: 'Vector3') -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(com.badlogic.gdx.math.Vector3)"""
        return float.__wrap(super(__Mesh, self).calculateRadius(arg0))

    @overload
    def getInstancedAttributes(self) -> 'VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.Mesh.getInstancedAttributes()"""
        return 'VertexAttributes'.__wrap(super(Mesh, self).getInstancedAttributes())

    @overload
    def getIndices(self, arg0: 'short', arg1: int):
        """public void com.badlogic.gdx.graphics.Mesh.getIndices(short[],int)"""
        super(__Mesh, self).getIndices(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def transform(arg0: 'Matrix4', arg1: 'float', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static void com.badlogic.gdx.graphics.Mesh.transform(com.badlogic.gdx.math.Matrix4,float[],int,int,int,int,int)"""
        __Mesh.transform(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @overload
    def calculateBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int, arg3: 'Matrix4') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.calculateBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int,com.badlogic.gdx.math.Matrix4)"""
        return 'collision.BoundingBox'.__wrap(super(__Mesh, self).calculateBoundingBox(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,float[])"""
        return 'Mesh'.__wrap(super(__Mesh, self).updateInstanceData(__int.valueOf(arg0), arg1))

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'float', arg2: int, arg3: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,float[],int,int)"""
        return 'Mesh'.__wrap(super(__Mesh, self).updateInstanceData(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def clearAllMeshes(arg0: 'Application'):
        """public static void com.badlogic.gdx.graphics.Mesh.clearAllMeshes(com.badlogic.gdx.Application)"""
        __Mesh.clearAllMeshes(arg0)

    @overload
    def unbind(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.Mesh.unbind(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__Mesh, self).unbind(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setInstanceData(self, arg0: 'FloatBuffer', arg1: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setInstanceData(java.nio.FloatBuffer,int)"""
        return 'Mesh'.__wrap(super(__Mesh, self).setInstanceData(arg0, __int.valueOf(arg1)))

    @overload
    def getVerticesBuffer(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.Mesh.getVerticesBuffer()"""
        return 'FloatBuffer'.__wrap(super(Mesh, self).getVerticesBuffer())

    @overload
    def setAutoBind(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.Mesh.setAutoBind(boolean)"""
        super(__Mesh, self).setAutoBind(__boolean.valueOf(arg0))

    @overload
    def disableInstancedRendering(self) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.disableInstancedRendering()"""
        return 'Mesh'.__wrap(super(Mesh, self).disableInstancedRendering())

    @overload
    def getVerticesBuffer(self, arg0: bool) -> 'FloatBuffer':
        """public java.nio.FloatBuffer com.badlogic.gdx.graphics.Mesh.getVerticesBuffer(boolean)"""
        return 'FloatBuffer'.__wrap(super(__Mesh, self).getVerticesBuffer(__boolean.valueOf(arg0)))

    @overload
    def setIndices(self, arg0: 'short') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.setIndices(short[])"""
        return 'Mesh'.__wrap(super(__Mesh, self).setIndices(arg0))

    @overload
    def getVertexAttributes(self) -> 'VertexAttributes':
        """public com.badlogic.gdx.graphics.VertexAttributes com.badlogic.gdx.graphics.Mesh.getVertexAttributes()"""
        return 'VertexAttributes'.__wrap(super(Mesh, self).getVertexAttributes())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def updateVertices(self, arg0: int, arg1: 'float') -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateVertices(int,float[])"""
        return 'Mesh'.__wrap(super(__Mesh, self).updateVertices(__int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def updateInstanceData(self, arg0: int, arg1: 'FloatBuffer', arg2: int, arg3: int) -> 'Mesh':
        """public com.badlogic.gdx.graphics.Mesh com.badlogic.gdx.graphics.Mesh.updateInstanceData(int,java.nio.FloatBuffer,int,int)"""
        return 'Mesh'.__wrap(super(__Mesh, self).updateInstanceData(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def transformUV(self, arg0: 'Matrix3'):
        """public void com.badlogic.gdx.graphics.Mesh.transformUV(com.badlogic.gdx.math.Matrix3)"""
        super(__Mesh, self).transformUV(arg0)

    @overload
    def calculateRadius(self, arg0: 'Vector3', arg1: int, arg2: int) -> float:
        """public float com.badlogic.gdx.graphics.Mesh.calculateRadius(com.badlogic.gdx.math.Vector3,int,int)"""
        return float.__wrap(super(__Mesh, self).calculateRadius(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def extendBoundingBox(self, arg0: 'BoundingBox', arg1: int, arg2: int, arg3: 'Matrix4') -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.Mesh.extendBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,int,int,com.badlogic.gdx.math.Matrix4)"""
        return 'collision.BoundingBox'.__wrap(super(__Mesh, self).extendBoundingBox(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: int, arg3: 'VertexAttributes'):
        """public com.badlogic.gdx.graphics.Mesh(boolean,int,int,com.badlogic.gdx.graphics.VertexAttributes)"""
        val = __Mesh(__boolean.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val