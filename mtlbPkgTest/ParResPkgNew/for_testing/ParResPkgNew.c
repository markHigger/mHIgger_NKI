/*
 * MATLAB Compiler: 6.5 (R2017b)
 * Date: Tue Aug 14 10:32:25 2018
 * Arguments:
 * "-B""macro_default""-W""lib:ParResPkgNew""-T""link:lib""-d""/Users/markhigger
 * /Documents/NKI/mHigger_NKI/mtlbPkgTest/ParResPkgNew/for_testing""-v""/Users/m
 * arkhigger/Documents/MATLAB/ParRes.m"
 */

#include <stdio.h>
#define EXPORTING_ParResPkgNew 1
#include "ParResPkgNew.h"

static HMCRINSTANCE _mcr_inst = NULL;

#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultPrintHandler(const char *s)
{
    return mclWrite(1 /* stdout */, s, sizeof(char)*strlen(s));
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

#ifdef __cplusplus
extern "C" {
#endif

static int mclDefaultErrorHandler(const char *s)
{
    int written = 0;
    size_t len = 0;
    len = strlen(s);
    written = mclWrite(2 /* stderr */, s, sizeof(char)*len);
    if (len > 0 && s[ len-1 ] != '\n')
        written += mclWrite(2 /* stderr */, "\n", sizeof(char));
    return written;
}

#ifdef __cplusplus
} /* End extern "C" block */
#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_ParResPkgNew_C_API
#define LIB_ParResPkgNew_C_API /* No special import/export declaration */
#endif

LIB_ParResPkgNew_C_API 
bool MW_CALL_CONV ParResPkgNewInitializeWithHandlers(
    mclOutputHandlerFcn error_handler,
    mclOutputHandlerFcn print_handler)
{
    int bResult = 0;
    if (_mcr_inst != NULL)
        return true;
    if (!mclmcrInitialize())
        return false;
    {
        mclCtfStream ctfStream = 
            mclGetEmbeddedCtfStream((void *)(ParResPkgNewInitializeWithHandlers));
        if (ctfStream) {
            bResult = mclInitializeComponentInstanceEmbedded(&_mcr_inst,
                                                             error_handler, 
                                                             print_handler,
                                                             ctfStream);
            mclDestroyStream(ctfStream);
        } else {
            bResult = 0;
        }
    }  
    if (!bResult)
    return false;
    return true;
}

LIB_ParResPkgNew_C_API 
bool MW_CALL_CONV ParResPkgNewInitialize(void)
{
    return ParResPkgNewInitializeWithHandlers(mclDefaultErrorHandler, 
                                            mclDefaultPrintHandler);
}

LIB_ParResPkgNew_C_API 
void MW_CALL_CONV ParResPkgNewTerminate(void)
{
    if (_mcr_inst != NULL)
        mclTerminateInstance(&_mcr_inst);
}

LIB_ParResPkgNew_C_API 
void MW_CALL_CONV ParResPkgNewPrintStackTrace(void) 
{
    char** stackTrace;
    int stackDepth = mclGetStackTrace(&stackTrace);
    int i;
    for(i=0; i<stackDepth; i++)
    {
        mclWrite(2 /* stderr */, stackTrace[i], sizeof(char)*strlen(stackTrace[i]));
        mclWrite(2 /* stderr */, "\n", sizeof(char)*strlen("\n"));
    }
    mclFreeStackTrace(&stackTrace, stackDepth);
}


LIB_ParResPkgNew_C_API 
bool MW_CALL_CONV mlxParRes(int nlhs, mxArray *plhs[], int nrhs, mxArray *prhs[])
{
    return mclFeval(_mcr_inst, "ParRes", nlhs, plhs, nrhs, prhs);
}

LIB_ParResPkgNew_C_API 
bool MW_CALL_CONV mlfParRes(int nargout, mxArray** R, mxArray* R1, mxArray* R2)
{
    return mclMlfFeval(_mcr_inst, "ParRes", nargout, 1, 2, R, R1, R2);
}

