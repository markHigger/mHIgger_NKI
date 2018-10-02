function CorMat = makeCorMat(data, numChans)
    CorMat = zeros(numChans);
    for chanYidx = 1:numChans
        for chanXidx = chanYidx:numChans
            if chanXidx ~= chanYidx
                corr = corr2(data(chanXidx, :), data(chanYidx, :));
                if abs(corr) >= 0
                    CorMat(chanXidx, chanYidx) = corr;
                end
            end
        end
    end
    CorMat = CorMat + CorMat';
end
