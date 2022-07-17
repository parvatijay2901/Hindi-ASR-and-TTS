from pathlib import Path

import numpy as np
import pytest
import scipy.io.wavfile

from pesq import pesq, pesq_batch, NoUtterancesError, PesqError


def test():
    ref_path = 'speech.wav'
    deg_path = 'speech_bab_0dB.wav'

    sample_rate, ref = scipy.io.wavfile.read(ref_path)
    sample_rate, deg = scipy.io.wavfile.read(deg_path)

    score = pesq(ref=ref, deg=deg, fs=sample_rate, mode='wb')

    assert score == 1.0832337141036987, score

    score = pesq(ref=ref, deg=deg, fs=sample_rate, mode='nb')

    assert score == 1.6072081327438354, score
    return score


def test_no_utterances_nb_mode():
    sample_rate = 16000
    silent_ref = np.zeros(sample_rate)
    deg = np.random.randn(sample_rate)

    with pytest.raises(NoUtterancesError) as e:
        pesq(ref=silent_ref, deg=deg, fs=sample_rate, mode='nb')

    score = pesq(ref=silent_ref, deg=deg, fs=sample_rate, mode='nb',
                 on_error=PesqError.RETURN_VALUES)

    assert score == PesqError.NO_UTTERANCES_DETECTED, score
    return score


def test_no_utterances_wb_mode():
    sample_rate = 16000
    silent_ref = np.zeros(sample_rate)
    deg = np.random.randn(sample_rate)

    with pytest.raises(NoUtterancesError) as e:
        pesq(ref=silent_ref, deg=deg, fs=sample_rate, mode='wb')

    score = pesq(ref=silent_ref, deg=deg, fs=sample_rate, mode='wb',
                 on_error=PesqError.RETURN_VALUES)

    assert score == PesqError.NO_UTTERANCES_DETECTED, score
    return score


def test_pesq_batch():
    ref_path = 'speech.wav'
    deg_path = 'speech_bab_0dB.wav'

    sample_rate, ref = scipy.io.wavfile.read(ref_path)
    sample_rate, deg = scipy.io.wavfile.read(deg_path)

    n_file = 10
    ideally = np.array([1.0832337141036987 for i in range(n_file)])

    # 1D - 1D
    score = pesq_batch(ref=ref, deg=deg, fs=sample_rate, mode='wb')
    assert score == [1.0832337141036987], score

    # 1D - 2D
    deg_2d = np.repeat(deg[np.newaxis, :], n_file, axis=0)
    scores = pesq_batch(ref=ref, deg=deg_2d, fs=sample_rate, mode='wb')
    assert np.allclose(np.array(scores), ideally), scores

    # 2D - 2D
    ref_2d = np.repeat(ref[np.newaxis, :], n_file, axis=0)
    scores = pesq_batch(ref=ref_2d, deg=deg_2d, fs=sample_rate, mode='wb')
    assert np.allclose(np.array(scores), ideally), scores

    # narrowband
    score = pesq_batch(ref=ref, deg=deg, fs=sample_rate, mode='nb')
    assert score == [1.6072081327438354], score

    # 1D - 2D multiprocessing
    deg_2d = np.repeat(deg[np.newaxis, :], n_file, axis=0)
    scores = pesq_batch(ref=ref, deg=deg_2d, fs=sample_rate, mode='wb', n_processor=4)
    assert np.allclose(np.array(scores), ideally), scores

    # 2D - 2D multiprocessing
    ref_2d = np.repeat(ref[np.newaxis, :], n_file, axis=0)
    scores = pesq_batch(ref=ref_2d, deg=deg_2d, fs=sample_rate, mode='wb', n_processor=4)
    assert np.allclose(np.array(scores), ideally), scores
