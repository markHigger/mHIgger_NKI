/*
 * MATLAB Compiler: 6.5 (R2017b)
 * Date: Wed Aug 15 14:20:23 2018
 * Arguments:
 * "-B""macro_default""-W""lib:EEG_Preproc_test_v2_6""-T""link:lib""-d""/Users/m
 * arkhigger/Documents/NKI/mHigger_NKI/mtlbPkgTest/EEG_Preproc_test_v2_6/for_tes
 * ting""-v""/Users/markhigger/Documents/NKI/mHigger_NKI/EEG_Preprocessing/EEG_P
 * reprocess_Pipeline_mat.m""-a""/Users/markhigger/Documents/MATLAB/TOOLBOX/EEG_
 * PreProc_funs/fmrib1.21/fmrib_fastr.m"
 */

#ifndef __EEG_Preproc_test_v2_6_h
#define __EEG_Preproc_test_v2_6_h 1

#if defined(__cplusplus) && !defined(mclmcrrt_h) && defined(__linux__)
#  pragma implementation "mclmcrrt.h"
#endif
#include "mclmcrrt.h"
#ifdef __cplusplus
extern "C" {
#endif

/* This symbol is defined in shared libraries. Define it here
 * (to nothing) in case this isn't a shared library. 
 */
#ifndef LIB_EEG_Preproc_test_v2_6_C_API 
#define LIB_EEG_Preproc_test_v2_6_C_API /* No special import/export declaration */
#endif

/* GENERAL LIBRARY FUNCTIONS -- START */

extern LIB_EEG_Preproc_test_v2_6_C_API 
bool MW_CALL_CONV EEG_Preproc_test_v2_6InitializeWithHandlers(
       mclOutputHandlerFcn error_handler, 
       mclOutputHandlerFcn print_handler);

extern LIB_EEG_Preproc_test_v2_6_C_API 
bool MW_CALL_CONV EEG_Preproc_test_v2_6Initialize(void);

extern LIB_EEG_Preproc_test_v2_6_C_API 
void MW_CALL_CONV EEG_Preproc_test_v2_6Terminate(void);

extern LIB_EEG_Preproc_test_v2_6_C_API 
void MW_CALL_CONV EEG_Preproc_test_v2_6PrintStackTrace(void);

/* GENERAL LIBRARY FUNCTIONS -- END */

/* C INTERFACE -- MLX WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- START */

extern LIB_EEG_Preproc_test_v2_6_C_API 
bool MW_CALL_CONV mlxEEG_Preprocess_Pipeline_mat(int nlhs, mxArray *plhs[], int nrhs, 
                                                 mxArray *prhs[]);

/* C INTERFACE -- MLX WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- END */

/* C INTERFACE -- MLF WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- START */

extern LIB_EEG_Preproc_test_v2_6_C_API bool MW_CALL_CONV mlfEEG_Preprocess_Pipeline_mat(int nargout, mxArray** EEG_Resample, mxArray* filepath_input, mxArray* varargin);

#ifdef __cplusplus
}
#endif
/* C INTERFACE -- MLF WRAPPERS FOR USER-DEFINED MATLAB FUNCTIONS -- END */

#endif
