/*
 * MATLAB Compiler: 6.5 (R2017b)
 * Date: Wed Aug 15 16:39:19 2018
 * Arguments:
 * "-B""macro_default""-W""lib:EEG_Preproc_test_3_3""-T""link:lib""-d""/Users/ma
 * rkhigger/Documents/NKI/mHigger_NKI/mtlbPkgTest/EEG_Preproc_test_3_3/for_testi
 * ng""-v""/Users/markhigger/Documents/NKI/mHigger_NKI/EEG_Preprocessing/EEG_Pre
 * process_Pipeline_mat.m""-a""/Users/markhigger/Documents/MATLAB/TOOLBOX/EEG_Pr
 * eProc_funs/fmrib1.21/fmrib_fastr.m"
 */

#include <stdio.h>
#define EXPORTING_EEG_Preproc_test_3_3 1
#include "EEG_Preproc_test_3_3.h"

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
#ifndef LIB_EEG_Preproc_test_3_3_C_API
#define LIB_EEG_Preproc_test_3_3_C_API /* No special import/export declaration */
#endif

LIB_EEG_Preproc_test_3_3_C_API 
bool MW_CALL_CONV EEG_Preproc_test_3_3InitializeWithHandlers(
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
            mclGetEmbeddedCtfStream((void *)(EEG_Preproc_test_3_3InitializeWithHandlers));
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

LIB_EEG_Preproc_test_3_3_C_API 
bool MW_CALL_CONV EEG_Preproc_test_3_3Initialize(void)
{
    return EEG_Preproc_test_3_3InitializeWithHandlers(mclDefaultErrorHandler, 
                                                    mclDefaultPrintHandler);
}

LIB_EEG_Preproc_test_3_3_C_API 
void MW_CALL_CONV EEG_Preproc_test_3_3Terminate(void)
{
    if (_mcr_inst != NULL)
        mclTerminateInstance(&_mcr_inst);
}

LIB_EEG_Preproc_test_3_3_C_API 
void MW_CALL_CONV EEG_Preproc_test_3_3PrintStackTrace(void) 
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


LIB_EEG_Preproc_test_3_3_C_API 
bool MW_CALL_CONV mlxEEG_Preprocess_Pipeline_mat(int nlhs, mxArray *plhs[], int nrhs, 
                                                 mxArray *prhs[])
{
    return mclFeval(_mcr_inst, "EEG_Preprocess_Pipeline_mat", nlhs, plhs, nrhs, prhs);
}

LIB_EEG_Preproc_test_3_3_C_API 
bool MW_CALL_CONV mlfEEG_Preprocess_Pipeline_mat(int nargout, mxArray** EEG_Resample, 
                                                 mxArray* filepath_input, mxArray* 
                                                 varargin)
{
    return mclMlfFeval(_mcr_inst, "EEG_Preprocess_Pipeline_mat", nargout, 1, -2, EEG_Resample, filepath_input, varargin);
}

